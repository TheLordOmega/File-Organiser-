import argparse
from pathlib import Path

from scanner import organizer


def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by topic and file type."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Folder to organize (default: current directory).",
    )
    args = parser.parse_args()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.is_dir():
        parser.error(f"not a folder: {folder}")

    print(f"Organizing files in: {folder}")
    moved, errors = organizer(folder)

    if errors:
        print(f"Finished with {len(errors)} error(s); moved {moved} file(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Finished. Moved {moved} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
