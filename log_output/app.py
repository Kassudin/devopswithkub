import os
import uuid
from datetime import datetime, timezone

from flask import Flask

app = Flask(__name__)

random_string = str(uuid.uuid4())

def current_timestamp():
    return (
    datetime.now(timezone.utc)
    .isoformat()
    .replace('+00:00', 'Z')
    )

@app.route('/')
def index():
    timestamp = current_timestamp()
    output = f"{timestamp} - {random_string}"

    return output

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host="0.0.0.0", port=port)