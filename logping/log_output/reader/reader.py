import os
import urllib.request
from flask import Flask

app = Flask(__name__)

output_file = "/usr/src/app/files/output.txt"
information_file = "/config/information.txt"
pingpongurl = "http://ping-pong-svc:2345/pings"


def read_file(path, default):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        return default

def get_pong_count():
    with urllib.request.urlopen(pingpongurl) as response:
        return response.read().decode()


@app.route("/")
def index():
    output = read_file(
        output_file,
        "Waiting for log output..."
    )
    information = read_file(
        information_file,
        "No information available."
    )
    message = os.environ.get("MESSAGE", "")
    counter = get_pong_count()
    return (
        f"file content: {information}\n"
        f"env variable: MESSAGE={message}\n"
        f"{output}\n"
        f"Ping / Pongs: {counter}\n"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
