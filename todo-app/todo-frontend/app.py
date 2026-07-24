import os
import json
import time
import urllib.request

from flask import Flask, send_file, request, redirect


app = Flask(__name__)

image_url = "https://picsum.photos/1200"
image_file = "/usr/src/app/files/image.jpg"
backend_url = "http://todo-backend-svc:2345/todos"

cache_duration = 60 * 10

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

@app.route("/todo", methods=["GET","POST"])
def index():
    if request.method == "POST":
        todo = request.form["todo"]
        create_todo(todo)
        return redirect("/todo")
    todos = get_todos()
    todos_html = "".join(f"<li>{todo}</li>" for todo in todos)
    return f"""
    <h1>Todo app</h1>

    <img src="/todo/image" width="600" alt="Random image">

    <form method="POST">
        <input type="text" name="todo" maxlength="140">
        <button type="submit">Send</button>
    </form>
    <ul>
        {todos_html}
    </ul>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
