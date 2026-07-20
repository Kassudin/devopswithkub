import os

from flask import Flask

app = Flask(__name__)

counter_file = "/usr/src/app/files/counter.txt"

def read_counter():
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            return int(f.read().strip())
    else:
        return 0
    
def write_counter(value):
    with open(counter_file, "w") as f:
        f.write(str(value))


@app.route("/pingpong")
def pingpong():
    counter = read_counter()
    response = f"pong {counter}\n"
    write_counter(counter + 1)
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)