import os
import socket
import time

"""
The delay is 1 second. Therefore we will try for 30 seconds.
"""
MAX_RETRY_COUNT = 30

DATABASE_HOST = os.getenv("DATABASE_HOST", "postgres")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", 5432))


def wait_for_db():
    print("Waiting for DB")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    retry_count = 0
    while retry_count < MAX_RETRY_COUNT:
        try:
            s.connect((DATABASE_HOST, DATABASE_PORT))
            s.close()
            break
        except socket.error as ex:
            time.sleep(1)
            retry_count += 1

    # Raise a command error if we still aren't connected.
    if MAX_RETRY_COUNT == retry_count:
        raise Exception(
            f'Unable to connect to database: "{DATABASE_HOST}:{DATABASE_PORT}". '
            f"Make sure it is running or update acv_micro_apex.settings"
        )


if __name__ == "__main__":
    wait_for_db()
