from pathlib import Path
from datetime import datetime


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
