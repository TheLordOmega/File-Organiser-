from pathlib import Path
from pypdf import PdfReader

pdf_path = Path(__file__).parent / "test Orient.pdf"
md_path = pdf_path.with_suffix(".md")

reader = PdfReader(pdf_path)

markdown = [f"# {pdf_path.stem}\n"]

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text(extraction_mode="layout")

    if text and text.strip():
        markdown.append(f"## Page {page_number}\n\n{text.strip()}\n")

md_path.write_text("\n".join(markdown), encoding="utf-8")

print(f"Extracted {len(reader.pages)} pages to: {md_path}")
