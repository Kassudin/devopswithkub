import os

from flask import Flask

app = Flask(__name__)

file_path = "/usr/src/app/files/output.txt"


@app.route("/")
def index():
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read() + "\n"
    except FileNotFoundError:
        return "Waiting for log output...\n", 503


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)