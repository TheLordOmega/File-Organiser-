
from pathlib import Path

from pypdf import PdfReader


def pdf_to_markdown(pdf_path, md_path=None):
    pdf_path = Path(pdf_path)

    if md_path is None:
        md_path = pdf_path.with_suffix(".md")
    else:
        md_path = Path(md_path)

    reader = PdfReader(pdf_path)

    markdown = [f"# {pdf_path.stem}\n"]

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text(extraction_mode="layout")

        if text and text.strip():
            markdown.append(
                f"## Page {page_number}\n\n{text.strip()}\n"
            )

    md_path.write_text("\n".join(markdown), encoding="utf-8")

    print(f"Extracted {len(reader.pages)} pages to: {md_path}")

    return md_path
