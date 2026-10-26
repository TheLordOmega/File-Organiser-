from pathlib import Path
from datetime import datetime


directory = Path.cwd()

text_folder = Path("text_files")
text_folder.mkdir(exist_ok=True)
history_file = Path(text_folder /"history.md")

blacklist= {
    "history.md",
    ".wakatime-project",
    "Organiser.py",
    "main.py",
    "config.py",
    "scanner.py",
    "classifier.py",
    "organizer.py",
    "history.py",
    "pdf_tools.py",
    "cli.py",
    "cleanup.py",
    "pdf.py",
    "requirements.txt",
    "organizer.log",
}

topics = {
    "physics": ["physics", "thermodynamics", "fluids"],
    "maths": ["calculus", "algebra", "maths"],
}


if history_file.exists() and history_file.read_text(encoding="utf-8").strip():
    last_line = history_file.read_text(encoding="utf-8").strip().split("\n")[-1]
    print(f"Last line: {last_line}")
    date = datetime.strptime(last_line, "%Y-%m-%d %H:%M")
else:
    date = datetime.strptime(input("Enter a date (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")


with open(history_file, "a", encoding="utf-8") as f:
    f.write(date.now().strftime("%Y-%m-%d %H:%M") + "\n")
