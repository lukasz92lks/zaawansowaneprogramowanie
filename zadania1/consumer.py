import time
from contextlib import closing

from producer import connect


def claim_job(connection):
    with connection:
        connection.execute("BEGIN IMMEDIATE")
        job = connection.execute("""
            SELECT id FROM jobs
            WHERE status = 'pending'
            ORDER BY id
            LIMIT 1
        """).fetchone()

        if job is None:
            return None

        job_id = job[0]
        connection.execute(
            "UPDATE jobs SET status = 'in_progress' WHERE id = ?",
            (job_id,),
        )

    return job_id


def main():
    with closing(connect()) as connection:
        while True:
            job_id = claim_job(connection)

            if job_id is None:
                time.sleep(5)
                continue

            print(f"Rozpoczynam rozmowę {job_id}")
            time.sleep(30)

            with connection:
                connection.execute(
                    "UPDATE jobs SET status = 'done' WHERE id = ?",
                    (job_id,),
                )

            print(f"Zakończono rozmowę {job_id}")


if __name__ == "__main__":
    main()