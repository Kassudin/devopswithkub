import time
import uuid
from datetime import datetime, timezone

random_string = str(uuid.uuid4())
file_path = "/usr/src/app/files/output.txt"

while True:
    timestamp = (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )

    output = f"{timestamp}: {random_string}"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(output)

    print(output, flush=True)
    time.sleep(5)