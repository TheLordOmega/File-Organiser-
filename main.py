import argparse
from datetime import datetime
from pathlib import Path


from config import directory, history_file
from scanner import organizer
from pdf import extract_pdf, clean_markdown


def main():
    cutoff =

    scan_time = datetime.now()

    moved,errors = organize(
        directory,
        cutoff,
    )

    if errors == 0:
        save_cutoff(scan_time)
        print("History updated.")
    else:
        print("files failes, History not updated")
