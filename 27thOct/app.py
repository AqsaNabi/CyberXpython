import json
import os
import re
from datetime import datetime
from pathlib import Path

import streamlit as st
from chandra_parser import parse_pdf

BASE_DIR = Path(__file__).resolve().parent
PARSED_ROOT = BASE_DIR / "parsed_output"
PARSED_ROOT.mkdir(parents=True, exist_ok=True)

st.set_page_config(page_title="Chandra PDF Parser", page_icon="📄", layout="wide")
st.title("Chandra PDF Parser")
st.write("Upload a PDF, parse it, and inspect the saved files and JSON representation.")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Datalab API key", value=os.getenv("DATALAB_API_KEY", ""), type="password", help="Uses the environment variable if already set; the key is not written to output files.")
    extract_images = st.checkbox("Extract page images", value=True)
    image_width = st.number_input("Extracted image width (pixels)", min_value=200, max_value=2000, value=712, step=100, disabled=not extract_images)
    filter_figures = st.checkbox("Filter figures using OpenAI", value=False, help="Optional. Requires an OPENAI_API_KEY and may incur separate API costs.")
    openai_key = st.text_input("OpenAI API key", type="password") if filter_figures else ""

st.info(f"Parsed files are saved locally under: `{PARSED_ROOT}`. Parsing submits the PDF to Datalab's hosted API; only upload documents you are allowed to send.")
uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    st.write(f"**Selected file:** {uploaded_file.name} · {uploaded_file.size:,} bytes")
    if st.button("Parse PDF", type="primary", use_container_width=True):
        if not api_key.strip():
            st.error("Enter your Datalab API key in the sidebar or set DATALAB_API_KEY in PowerShell.")
        elif filter_figures and not openai_key.strip():
            st.error("Enter an OpenAI API key or turn off figure filtering.")
        else:
            os.environ["DATALAB_API_KEY"] = api_key.strip()
            if filter_figures:
                os.environ["OPENAI_API_KEY"] = openai_key.strip()
            safe_stem = re.sub(r"[^A-Za-z0-9._-]+", "_", Path(uploaded_file.name).stem).strip("._") or "document"
            run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
            document_dir = PARSED_ROOT / f"{safe_stem}_{run_id}"
            document_dir.mkdir(parents=True, exist_ok=False)
            pdf_path = document_dir / Path(uploaded_file.name).name
            output_dir = document_dir / "chandra_output"
            output_dir.mkdir(parents=True, exist_ok=True)
            pdf_path.write_bytes(uploaded_file.getvalue())
            try:
                with st.spinner("Sending PDF to Datalab and parsing it..."):
                    result = parse_pdf(str(pdf_path), str(output_dir), filter_figures=filter_figures, extract_images=extract_images, image_width=int(image_width))
                md_candidates = list(output_dir.rglob("*.md"))
                if isinstance(result, (str, Path)):
                    try:
                        rp = Path(result)
                        if rp.is_file() and rp.suffix.lower() == ".md" and rp not in md_candidates:
                            md_candidates.insert(0, rp)
                    except (TypeError, OSError):
                        pass
                markdown_path = md_candidates[0] if md_candidates else None
                markdown_text = markdown_path.read_text(encoding="utf-8", errors="replace") if markdown_path else ""
                generated_files = []
                for item in sorted(document_dir.rglob("*")):
                    if item.is_file() and item.name != "document.json":
                        generated_files.append({"path": str(item.relative_to(document_dir)).replace("\\", "/"), "file_name": item.name, "extension": item.suffix.lower(), "size_bytes": item.stat().st_size})
                # Wrapper JSON: Markdown content + metadata + file inventory. Not native block-level parser JSON.
                document_json = {
                    "source_document": {"file_name": pdf_path.name, "file_size_bytes": pdf_path.stat().st_size},
                    "parser": "chandra-parser",
                    "parsed_at": datetime.now().astimezone().isoformat(),
                    "output_format": "markdown_with_file_inventory",
                    "markdown_file": str(markdown_path.relative_to(document_dir)).replace("\\", "/") if markdown_path else None,
                    "markdown_content": markdown_text,
                    "files": generated_files,
                }
                json_path = document_dir / "document.json"
                json_path.write_text(json.dumps(document_json, ensure_ascii=False, indent=2), encoding="utf-8")
                st.session_state["parsed_document_dir"] = str(document_dir)
                st.session_state["parsed_markdown"] = markdown_text
                st.session_state["parsed_json"] = json.dumps(document_json, ensure_ascii=False, indent=2)
                if markdown_path:
                    st.success(f"Parsing completed. Files saved to: {document_dir}")
                else:
                    st.warning("Parser returned, but no Markdown file was found. The source PDF and any parser artifacts are still saved.")
                st.rerun()
            except Exception as exc:
                st.error(f"Parsing failed: {exc}")
                st.caption(f"The uploaded PDF and any partial output remain in: {document_dir}")

saved_dir_text = st.session_state.get("parsed_document_dir")
if saved_dir_text and Path(saved_dir_text).exists():
    saved_dir = Path(saved_dir_text)
    st.divider()
    st.subheader("Saved document structure")
    st.code(str(saved_dir), language="text")
    st.markdown("**Folder layout**")
    tree_lines = [saved_dir.name + "/"]
    for item in sorted(saved_dir.rglob("*")):
        rel = item.relative_to(saved_dir)
        tree_lines.append("  " * len(rel.parts) + rel.name + ("/" if item.is_dir() else ""))
    st.code("\n".join(tree_lines), language="text")
    tabs = st.tabs(["Markdown preview", "JSON structure", "Saved files"])
    with tabs[0]:
        markdown_text = st.session_state.get("parsed_markdown", "")
        if markdown_text:
            st.markdown(markdown_text)
            st.download_button("Download Markdown", markdown_text.encode("utf-8"), file_name="parsed_document.md", mime="text/markdown")
        else:
            st.write("No Markdown output was found for this parse.")
    with tabs[1]:
        json_text = st.session_state.get("parsed_json", "{}")
        st.json(json.loads(json_text))
        st.download_button("Download document.json", json_text.encode("utf-8"), file_name="document.json", mime="application/json")
        st.caption("document.json wraps the Markdown and lists generated files. It is not native element-by-element JSON from Chandra.")
    with tabs[2]:
        for item in sorted(saved_dir.rglob("*")):
            if item.is_file():
                rel = item.relative_to(saved_dir)
                st.write(f"**{rel.as_posix()}** · {item.stat().st_size:,} bytes")
                if item.suffix.lower() in {".md", ".json", ".txt"}:
                    data = item.read_text(encoding="utf-8", errors="replace")
                    st.download_button(f"Download {item.name}", data.encode("utf-8"), file_name=item.name, mime="application/json" if item.suffix.lower() == ".json" else "text/plain", key=f"download_{item.relative_to(saved_dir).as_posix()}")
st.caption("Tip: `parsed_output` is created next to app.py. Keep it out of Git if it may contain private documents.")
