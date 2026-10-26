from datetime import datetime
from pathlib import Path
from pypdf import PdfReader
from config import blacklist, text_folder, directory, topics, date




for file in directory.iterdir():
    if (
        file.is_file() and file.name not in blacklist
        and not file.name.startswith(".")
        and file.stat().st_mtime > date.timestamp()
    ):
        title = file.name.lower()
        if file.suffix.lower() in [".txt", ".md" ]:
            title += "" + file.read_text(encoding="utf-8", errors="ignore").lower()

        topic ="Other"
        for topic_name, keywords in topics.items():
            if any(keyword in title for keyword in keywords):
                topic = topic_name
                break
        else:
             print("No keywords found for {file.name}. File was moved to 'other'. ")

        file_type= file.suffix.lower().lstrip(".") or "no_extension"
        destination_folder = text_folder / topic / file_type
        destination_folder.mkdir(parents=True, exist_ok=True)
        new_path = destination_folder / file.name


        counter = 0
        while new_path.exists():
            counter += 1
            new_path = destination_folder/f"{file.stem}_{counter}{file.suffix}"
        file.rename(new_path)
        print(f"{file.name}-> {new_path}")




###if its a pdf


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
