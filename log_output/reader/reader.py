import os

from flask import Flask

app = Flask(__name__)

output_file = "/usr/src/app/files/output.txt"
counter_file = "/usr/src/app/files/counter.txt"

def read_file(path, default):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        return default

@app.route("/")
def index():
    output = read_file(
        output_file,
        "Waiting for log output..."
    )
    counter = read_file(
        counter_file,
        "0"
    )
    return f"{output}\nPing / Pongs: {counter}\n"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
