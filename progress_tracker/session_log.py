"""
Simple CLI logger for AI & coding sessions.

Usage:
    python progress_tracker/session_log.py
"""

import csv
from datetime import datetime
from pathlib import Path

# CSV file will live next to this script
LOG_FILE = Path(__file__).with_name("sessions.csv")


def ask(prompt: str, default: str | None = None) -> str:
    """Ask for input with an optional default value."""
    if default:
        raw = input(f"{prompt} [{default}]: ").strip()
        return raw or default
    return input(f"{prompt}: ").strip()


def main() -> None:
    # Default date = today
    today_str = datetime.now().strftime("%Y-%m-%d")

    print("\n=== Log a work session ===")
    date = ask("Date", today_str)
    session_type = ask("Session type (Learning / Building / Debugging / Planning / Career)")
    project = ask("Project / Topic")
    time_spent = ask("Time spent (minutes)")
    what_i_did = ask("What did you do? (1–3 sentences)")
    tools_used = ask("Tools used (comma-separated, e.g. Python, VS Code, Git, Notion)")
    artifacts = ask("Artifacts / Links (comma-separated URLs, optional)")
    notes = ask("Notes / Reflections (optional)")

    row = [
        date,
        session_type,
        project,
        time_spent,
        what_i_did,
        tools_used,
        artifacts,
        notes,
    ]

    # Create file if it does not exist, write header once
    file_exists = LOG_FILE.exists()
    with LOG_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(
                [
                    "date",
                    "session_type",
                    "project",
                    "time_spent_min",
                    "what_i_did",
                    "tools_used",
                    "artifacts_links",
                    "notes",
                ]
            )
        writer.writerow(row)

    print(f"\nSaved session to: {LOG_FILE.resolve()}\n")


if __name__ == "__main__":
    main()
