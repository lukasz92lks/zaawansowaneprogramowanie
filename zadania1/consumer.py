
import time
from pathlib import Path
from filelock import FileLock

QUEUE_FILE = Path(__file__).parent / "queue.txt"
LOCK_FILE = str(QUEUE_FILE) + ".lock"

while True:
    job_name = None

    with FileLock(LOCK_FILE):
        if QUEUE_FILE.exists():
            jobs = QUEUE_FILE.read_text(
                encoding="utf-8"
            ).splitlines()
        else:
            jobs = []

        for i, job in enumerate(jobs):
            name, status = job.split(";")

            if status == "pending":
                jobs[i] = f"{name};in_progress"
                job_name = name
                break

        if job_name is not None:
            QUEUE_FILE.write_text(
                "\n".join(jobs) + "\n",
                encoding="utf-8"
            )

    if job_name is None:
        print("Brak zadan, sprawdzam za 5 sekund")
        time.sleep(5)
        continue

    print(f"Rozpoczynam: {job_name}")
    time.sleep(30)

    with FileLock(LOCK_FILE):
        jobs = QUEUE_FILE.read_text(
            encoding="utf-8"
        ).splitlines()

        for i, job in enumerate(jobs):
            name, status = job.split(";")

            if name == job_name and status == "in_progress":
                jobs[i] = f"{name};done"
                break

        QUEUE_FILE.write_text(
            "\n".join(jobs) + "\n",
            encoding="utf-8"
        )

    print(f"Zakonczono: {job_name}")
