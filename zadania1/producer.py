
import sys
from pathlib import Path
from filelock import FileLock

QUEUE_FILE = Path(__file__).parent / "queue.txt"
LOCK_FILE = str(QUEUE_FILE) + ".lock"

count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

with FileLock(LOCK_FILE):
    if QUEUE_FILE.exists():
        jobs = QUEUE_FILE.read_text(
            encoding="utf-8"
        ).splitlines()
    else:
        jobs = []

    for _ in range(count):
        number = len(jobs) + 1
        jobs.append(f"Rozmowa {number};pending")

    QUEUE_FILE.write_text(
        "\n".join(jobs) + "\n",
        encoding="utf-8"
    )

print(f"Dodano {count} zadan do kolejki")
