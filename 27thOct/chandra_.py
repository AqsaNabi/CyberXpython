from chandra_parser import parse_pdf

# Full pipeline
result = parse_pdf(
    "document.pdf",
    "./output",
    filter_figures=True,  # Requires OPENAI_API_KEY
    extract_images=True,
    image_width=712,
)

# Individual functions
from chandra_parser import extract_page_images, filter_pages

extract_page_images("document.pdf", "./images", width=712)
print(result)