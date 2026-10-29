import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

import requests
import streamlit as st


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
PARSED_ROOT = BASE_DIR / "parsed_output"
PARSED_ROOT.mkdir(parents=True, exist_ok=True)

API_URL = "https://www.datalab.to/api/v1/marker"


# --------------------------------------------------
# STREAMLIT PAGE
# --------------------------------------------------

st.set_page_config(
    page_title="Marker PDF Parser",
    page_icon="📄",
    layout="wide",
)

st.title("Marker PDF Parser")

st.write(
    "Upload a PDF and parse it using Datalab's hosted Marker API. "
    "Inspect and download the resulting Markdown and JSON, and measure "
    "the end-to-end parsing time."
)


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def safe_filename(filename):
    """Create a safe folder name from the PDF filename."""
    stem = Path(filename).stem
    stem = re.sub(r"[^A-Za-z0-9._-]+", "_", stem).strip("._")
    return stem or "document"


def request_json(response):
    """Parse an HTTP response as JSON."""
    try:
        data = response.json()
    except ValueError as exc:
        raise RuntimeError(
            f"The API returned a non-JSON response "
            f"(HTTP {response.status_code}). "
            f"Response: {response.text[:1000]}"
        ) from exc

    if not response.ok:
        message = (
            data.get("error")
            or data.get("message")
            or response.text[:1000]
        )
        raise RuntimeError(
            f"API request failed (HTTP {response.status_code}): {message}"
        )

    return data


def parse_pdf_with_api(
    pdf_path,
    api_key,
    mode,
    force_ocr,
    timeout_seconds=600,
):
    """
    Submit a PDF to Datalab Marker and poll until processing finishes.

    The elapsed time measured by the caller includes upload, API/server
    processing, polling intervals, and network latency.
    """
    headers = {"X-Api-Key": api_key}

    with pdf_path.open("rb") as pdf_file:
        form_data = {
            "file": (
                pdf_path.name,
                pdf_file,
                "application/pdf",
            ),
            "output_format": (None, "markdown"),
            "mode": (None, mode),
            "force_ocr": (None, str(force_ocr).lower()),
        }

        with requests.post(
            API_URL,
            headers=headers,
            files=form_data,
            timeout=120,
        ) as response:
            data = request_json(response)

    if data.get("success") is False:
        raise RuntimeError(data.get("error") or "PDF submission failed.")

    check_url = data.get("request_check_url")
    if not check_url:
        raise RuntimeError(
            "The API response did not contain a request_check_url. "
            "Response: " + json.dumps(data, ensure_ascii=False)[:1500]
        )

    deadline = time.monotonic() + timeout_seconds

    while time.monotonic() < deadline:
        time.sleep(2)

        with requests.get(
            check_url,
            headers=headers,
            timeout=60,
        ) as response:
            result = request_json(response)

        status = str(result.get("status", "")).lower()

        if status == "complete":
            markdown = result.get("markdown")

            if not markdown:
                output = result.get("output")
                if isinstance(output, dict):
                    markdown = output.get("markdown")

            if not markdown:
                raise RuntimeError(
                    "Parsing completed, but no Markdown field was found. "
                    "Available fields: " + ", ".join(result.keys())
                )

            return markdown, result

        if status in {"failed", "error"}:
            raise RuntimeError(
                result.get("error") or "The Marker parsing job failed."
            )

    raise TimeoutError(
        "Marker did not finish within the configured "
        f"{timeout_seconds}-second timeout."
    )


def create_file_inventory(document_dir):
    """List saved files, excluding the wrapper JSON."""
    files = []

    for item in sorted(document_dir.rglob("*")):
        if not item.is_file() or item.name == "document.json":
            continue

        files.append(
            {
                "path": item.relative_to(document_dir).as_posix(),
                "file_name": item.name,
                "extension": item.suffix.lower(),
                "size_bytes": item.stat().st_size,
            }
        )

    return files


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.header("Settings")

    api_key = st.text_input(
        "Datalab API key",
        value=os.getenv("DATALAB_API_KEY", ""),
        type="password",
        help="Your key is sent to Datalab for authentication.",
    )

    mode = st.selectbox(
        "Parsing mode",
        options=["fast", "balanced"],
        index=0,
    )

    force_ocr = st.checkbox(
        "Force OCR",
        value=False,
        help="Use OCR even when the PDF contains an existing text layer.",
    )

    st.caption(
        "PDFs are uploaded to Datalab's hosted API. "
        "Do not upload documents unless you are authorized to share them."
    )


# --------------------------------------------------
# PDF UPLOAD AND PARSING
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload a PDF document",
    type=["pdf"],
)

if uploaded_file:
    st.write(
        f"**Selected file:** {uploaded_file.name} "
        f"· {uploaded_file.size:,} bytes"
    )

    if st.button("Parse PDF", type="primary", use_container_width=True):
        if not api_key.strip():
            st.error(
                "Enter your Datalab API key in the sidebar or set "
                "the DATALAB_API_KEY environment variable."
            )
        elif uploaded_file.size == 0:
            st.error("The uploaded PDF is empty.")
        else:
            safe_stem = safe_filename(uploaded_file.name)
            run_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            document_dir = PARSED_ROOT / f"{safe_stem}_{run_id}"

            try:
                document_dir.mkdir(parents=True, exist_ok=False)

                pdf_path = document_dir / Path(uploaded_file.name).name
                pdf_path.write_bytes(uploaded_file.getvalue())

                # End-to-end timer: includes upload, server processing,
                # polling waits, and network latency.
                start_time = time.perf_counter()

                with st.spinner(
                    "Uploading PDF to Datalab and waiting for Marker to finish..."
                ):
                    markdown_text, api_result = parse_pdf_with_api(
                        pdf_path=pdf_path,
                        api_key=api_key.strip(),
                        mode=mode,
                        force_ocr=force_ocr,
                    )

                parsing_time_seconds = time.perf_counter() - start_time

                # Save Markdown output.
                markdown_path = document_dir / "parsed_document.md"
                markdown_path.write_text(markdown_text, encoding="utf-8")

                # Save the raw completed API response.
                raw_json_path = document_dir / "marker_response.json"
                raw_json_path.write_text(
                    json.dumps(api_result, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )

                # Build metadata JSON, including measured elapsed time.
                document_json = {
                    "source_document": {
                        "file_name": pdf_path.name,
                        "file_size_bytes": pdf_path.stat().st_size,
                    },
                    "parser": "datalab-hosted-marker",
                    "parsed_at": datetime.now().astimezone().isoformat(),
                    "parsing_time_seconds": round(parsing_time_seconds, 3),
                    "settings": {
                        "mode": mode,
                        "force_ocr": force_ocr,
                    },
                    "output_format": "markdown_with_file_inventory",
                    "markdown_file": "parsed_document.md",
                    "markdown_content": markdown_text,
                    "files": create_file_inventory(document_dir),
                }

                json_text = json.dumps(
                    document_json,
                    ensure_ascii=False,
                    indent=2,
                )

                json_path = document_dir / "document.json"
                json_path.write_text(json_text, encoding="utf-8")

                # Keep results in session state across st.rerun().
                st.session_state["parsed_document_dir"] = str(document_dir)
                st.session_state["parsed_markdown"] = markdown_text
                st.session_state["parsed_json"] = json_text
                st.session_state["marker_api_response"] = json.dumps(
                    api_result,
                    ensure_ascii=False,
                    indent=2,
                )
                st.session_state["parsing_time_seconds"] = parsing_time_seconds
                st.session_state["marker_error"] = None

                st.success(f"Parsing completed. Files saved to: {document_dir}")
                st.rerun()

            except Exception as exc:
                st.session_state["marker_error"] = str(exc)
                st.error(f"Parsing failed: {exc}")
                st.caption(
                    "Check the error details and your Datalab account's API limits."
                )


# --------------------------------------------------
# DISPLAY ERRORS
# --------------------------------------------------

if st.session_state.get("marker_error"):
    st.error(st.session_state["marker_error"])


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

saved_dir_text = st.session_state.get("parsed_document_dir")

if saved_dir_text and Path(saved_dir_text).exists():
    saved_dir = Path(saved_dir_text)

    st.divider()
    st.subheader("Parsing benchmark")

    parsing_time = st.session_state.get("parsing_time_seconds")
    if parsing_time is not None:
        st.metric("End-to-end parsing time", f"{parsing_time:.2f} seconds")
        st.caption(
            "Includes PDF upload, server-side processing, polling intervals, "
            "and network latency; it is not server-only processing time."
        )

    # Show basic document characteristics alongside the timing.
    source_pdf = next(
        (
            item for item in saved_dir.iterdir()
            if item.is_file() and item.suffix.lower() == ".pdf"
        ),
        None,
    )

    if source_pdf:
        col1, col2 = st.columns(2)
        col1.metric("PDF size", f"{source_pdf.stat().st_size / 1024:.1f} KB")
        col2.metric("PDF file", source_pdf.name)

    st.subheader("Saved document structure")
    st.code(str(saved_dir), language="text")

    tree_lines = [saved_dir.name + "/"]
    for item in sorted(saved_dir.rglob("*")):
        relative_path = item.relative_to(saved_dir)
        indentation = "  " * len(relative_path.parts)
        suffix = "/" if item.is_dir() else ""
        tree_lines.append(indentation + item.name + suffix)

    st.code("\n".join(tree_lines), language="text")

    tabs = st.tabs(
        ["Markdown preview", "JSON structure", "Saved files", "API response"]
    )

    with tabs[0]:
        markdown_text = st.session_state.get("parsed_markdown", "")
        st.markdown(markdown_text)
        st.download_button(
            "Download Markdown",
            data=markdown_text.encode("utf-8"),
            file_name="parsed_document.md",
            mime="text/markdown",
        )

    with tabs[1]:
        json_text = st.session_state.get("parsed_json", "{}")
        st.json(json.loads(json_text))
        st.download_button(
            "Download document.json",
            data=json_text.encode("utf-8"),
            file_name="document.json",
            mime="application/json",
        )
        st.caption(
            "This JSON contains the Markdown and file inventory. "
            "It is not the native block-by-block JSON representation."
        )

    with tabs[2]:
        for item in sorted(saved_dir.rglob("*")):
            if not item.is_file():
                continue

            relative_path = item.relative_to(saved_dir)
            st.write(
                f"**{relative_path.as_posix()}** "
                f"· {item.stat().st_size:,} bytes"
            )
            st.download_button(
                f"Download {item.name}",
                data=item.read_bytes(),
                file_name=item.name,
                mime="application/octet-stream",
                key="download_" + relative_path.as_posix(),
            )

    with tabs[3]:
        response_text = st.session_state.get("marker_api_response", "{}")
        st.json(json.loads(response_text))
        st.download_button(
            "Download raw API response",
            data=response_text.encode("utf-8"),
            file_name="marker_response.json",
            mime="application/json",
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Tip: parsed_output is created next to app.py. "
    "Keep private documents and API responses out of Git."
)
