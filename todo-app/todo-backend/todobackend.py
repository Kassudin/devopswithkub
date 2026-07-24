import os

from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    "Learn Kubernetes"
]

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    todo = data["todo"]
    if len (todo) > 140:
        return "Maximum length of todo is 140", 400
    todos.append(todo)
    return "Todo created", 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)