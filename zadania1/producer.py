import sqlite3
from contextlib import closing
from pathlib import Path

DATABASE = Path(__file__).with_name("queue.db")


def connect():
    connection = sqlite3.connect(DATABASE, timeout=10)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            status TEXT NOT NULL
                CHECK (status IN ('pending', 'in_progress', 'done'))
        )
    """)
    return connection


def main():
    with closing(connect()) as connection:
        with connection:
            cursor = connection.execute(
                "INSERT INTO jobs (status) VALUES (?)", ("pending",)
            )
            job_id = cursor.lastrowid

    print(f"Dodano rozmowę {job_id}")


if __name__ == "__main__":
    main()