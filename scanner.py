from config import blacklist, date, directory, text_folder, topics

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
