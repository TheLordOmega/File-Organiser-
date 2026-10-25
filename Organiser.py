from datetime import datetime
from pathlib import Path

from pypdf import PdfReader

##Inisialisation:
text_folder = Path("text_files")
text_folder.mkdir(exist_ok=True)

blacklist = ["history.md", ".wakatime-project", "Organiser.py","main.py"]
directory = Path.cwd()

#want to automate this to folder existing themes and folder structure
history_file = text_folder / "history.md"
if history_file.exists() and history_file.read_text(encoding="utf-8").strip():
    last_line = history_file.read_text(encoding="utf-8").strip().split("\n")[-1]
    print(f"Last line: {last_line}")
    date = datetime.strptime(last_line, "%Y-%m-%d %H:%M")
else:
    date = datetime.strptime(input("Enter a date (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")

topics = {
    "physics": ["physics", "thermodynamics", "fluids"],
    "maths": ["calculus", "algebra", "maths"],
}


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

with open(history_file, "a", encoding="utf-8") as f:
    f.write(date.now().strftime("%Y-%m-%d %H:%M") + "\n")




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


 #clean up lines
md_path = Path(__file__).parent / "test Orient.md"
output_path= md_path.with_name(f"{md_path.stem}_clean.md")

text= md_path.read_text(encoding="utf-8")

text= text.replace("\x0c","\n")

lines = [line.strip() for line in text.splitlines()]

cleaned_lines= []

for line in lines:
    if line:
        cleaned_lines.append(line)
    elif cleaned_lines and cleaned_lines[-1] !="":
        cleaned_lines.append("")

while cleaned_lines and cleaned_lines [-1] == "":
    cleaned_lines.pop()

output_path.write_text(
    "\n".join(cleaned_lines)+ "\n",
    encoding="utf-8"
)
print(f"Cleaned Makrdown saved to :{output_path}")
