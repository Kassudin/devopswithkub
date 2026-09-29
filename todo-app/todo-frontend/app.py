import os
import json
import time
import urllib.request
from flask import Flask, send_file, request, redirect
import requests


app = Flask(__name__)

image_url = os.environ["IMAGE_URL"]
image_file = os.environ["IMAGE_FILE"]
backend_url = os.environ["BACKEND_URL"]
cache_duration = int(os.environ["CACHE_DURATION"])
break_url = os.environ["BREAK_URL"]

def image_is_expired():
    if not os.path.exists(image_file):
        return True
    return time.time() - os.path.getmtime(image_file) > cache_duration

def download_image():
    urllib.request.urlretrieve(image_url, image_file)

@app.route("/todo/image")
def image():
    if image_is_expired():
        download_image()
    return send_file(image_file, mimetype="image/jpeg")

def get_todos():
    with urllib.request.urlopen(backend_url) as response:
        return json.loads(response.read().decode())

def create_todo(todo):
    data = json.dumps({"todo": todo}).encode()

    req = urllib.request.Request(
        backend_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    urllib.request.urlopen(req)

def update_todo(todo_id):
    req = urllib.request.Request(
        f"{backend_url}/{todo_id}",
        method="PUT"
    )
    urllib.request.urlopen(req)

@app.route("/todo/<int:todo_id>/done", methods=["POST"])
def mark_done(todo_id):
    update_todo(todo_id)
    return redirect("/todo")

def unhealthy_page():
    return """
    <html>
        <head>
            <title>System failure</title>
        </head>
        <body>
            <h1>System failure</h1>
            <p>The Todo app is currently unhealthy.</p>
            <p>Please wait for recovery.</p>
        </body>
    </html>
    """, 503


@app.route("/todo", methods=["GET","POST"])
def index():
    if request.method == "POST":
        todo = request.form["todo"]
        create_todo(todo)
        return redirect("/todo")
    todos = get_todos()
    todo_items = []
    for todo in todos:
        if todo["done"]:
            todo_items.append(
                f"<li>{todo['todo']} - Done</li>"
            )
        else:
            todo_items.append(f"""
                <li>
                    {todo["todo"]}
                    <form action="/todo/{todo["id"]}/done"
                        method="POST"
                        style="display:inline;">
                        <button type="submit">Done</button>
                    </form>
                </li>
            """)

    todos_html = "".join(todo_items)
    return f"""
    <h1>Todo app</h1>

    <img src="/todo/image" width="600" alt="Random image">

    <form method="POST">
        <input type="text" name="todo" maxlength="140">
        <button type="submit">Send</button>
    </form>
    <form action="/todo/break" method="POST">
        <button type="submit">Break app</button>
    </form>
    <ul>
        {todos_html}
    </ul>
    """

@app.route("/")
def health():
    return "Works", 200

@app.route("/todo/break", methods=["POST"])
def break_app():
    try:
        requests.post(
            break_url,
            timeout=2
        )
    except requests.RequestException:
        pass
    return unhealthy_page()

if __name__ == "__main__":
    port = int(os.environ["PORT"])
    app.run(host="0.0.0.0", port=port)