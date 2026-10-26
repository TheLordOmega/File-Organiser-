from pathlib import Path

from config import blacklist, load_last_run, save_last_run, text_folder, topics


def organizer(folder):
    """Organize files directly inside folder; return (moved_count, errors)."""
    directory = Path(folder).expanduser().resolve()
    moved = 0
    errors = []

    if not directory.is_dir():
        return 0, [f"Folder does not exist: {directory}"]

    try:
        last_run = load_last_run(directory)
        files = sorted(directory.iterdir())
    except (OSError, ValueError) as error:
        return 0, [f"Could not read folder history or contents: {error}"]

    ignored_names = {name.casefold() for name in blacklist}

    for file in files:
        if not file.is_file():
            continue
        if file.name.startswith(".") or file.name.casefold() in ignored_names:
            continue

        try:
            if last_run is not None and file.stat().st_mtime <= last_run.timestamp():
                continue

            searchable_text = file.name.casefold()
            if file.suffix.casefold() in {".txt", ".md"}:
                searchable_text += file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                ).casefold()

            topic = "Other"
            for topic_name, keywords in topics.items():
                if any(keyword.casefold() in searchable_text for keyword in keywords):
                    topic = topic_name
                    break

            file_type = file.suffix.casefold().lstrip(".") or "no_extension"
            destination_folder = directory / text_folder / topic / file_type
            destination_folder.mkdir(parents=True, exist_ok=True)

            destination = destination_folder / file.name
            counter = 0
            while destination.exists():
                counter += 1
                destination = destination_folder / (
                    f"{file.stem}_{counter}{file.suffix}"
                )

            file.rename(destination)
            moved += 1
            print(f"{file.name} -> {destination}")

        except OSError as error:
            errors.append(f"Could not process {file.name}: {error}")

    if moved > 0 and not errors:
        try:
            save_last_run(directory)
        except OSError as error:
            errors.append(f"Could not save history: {error}")

    return moved, errors
