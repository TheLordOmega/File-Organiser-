from pathlib import Path

from config import blacklist, load_last_run, save_last_run, text_folder, topics


def organizer(folder):
    directory = Path(folder).expanduser().resolve()
    moved = 0
    errors =[]

    if not directory.is_dir():
        return 0, [f"Folder does not exist: {directory}"]

    try:
        date = load_last_run(directory)
        files = sorted(directory.iterdir())

    except (OSError, ValueError) as error:
        return 0, [f"Could not read folder History: {error}"]

    for file in files:
        if not file.is_file():
            continue
        if file.name in blacklist or file.name.startswith("."):
            continue
        try:
            if date is not None and file.stat().st_mtime <= date.timestamp():
                continue

            title = file.name.lower()

            if file.suffix.lower() in [".txt", ".md" ]:
                title += "" + file.read_text(encoding="utf-8", errors="ignore").lower()

            topic ="Other"
            for topic_name, keywords in topics.items():
                if any(keyword in title for keyword in keywords):
                    topic = topic_name
                    break

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
        except OSError as error:
            errors.append(f"Could not save history: {error}")
    if moved > 0 and not errors:
        try:
            save_last_run(directory)
        except OSError as error:
            errors.append(f"Could not save history: {error}")

    return moved, errors
