from datetime import datetime
from pathlib import Path

directory = Path.cwd()

text_folder = Path("text_files")
text_folder.mkdir(exist_ok=True)
history_file = text_folder /"history.md"

blacklist = {
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
    "ui.py",
    "README.md",
}

topics = {
    "physics": ["physics", "thermodynamics", "fluids"],
    "maths": ["calculus", "algebra", "maths"],
}

def history_path(folder):
    return Path(folder)/ history_file

def load_last_run(folder):
    path = history_path(folder)

    if not path.exists():
        return None

    lines= path.read_text(encoding="utf-8").splitlines()

    for line in reversed(lines):
        line = line.strip()
        if line:
            return datetime.fromisoformat(line)
    return None


def save_last_run(folder):
    path = history_path(folder)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open( "a", encoding = "utf-8") as history:
        history.write(datetime.now().isoformat(timespec="seconds") +"\n")
