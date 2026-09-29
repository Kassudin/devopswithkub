import os
import psycopg2
from flask import Flask, jsonify, request
app = Flask(__name__)
database_url = os.environ["DATABASE_URL"]
is_healthy = True

def init_db():
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            todo TEXT NOT NULL
            done BOOLEAN NOT NULL DEFAULT FALSE
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

@app.route("/todos", methods=["GET"])
def get_todos():
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    cursor.execute("SELECT id, todo, done FROM todos ORDER BY id")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    todos = [{"id": row[0], "todo": row[1], "done": row[2]} for row in rows]
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    todo = data["todo"]
    print(f"Todo received: {todo}", flush=True)
    if len (todo) > 140:
        print(f"Todo rejected: {todo}", flush=True)
        return "Maximum length of todo is 140", 400
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO todos (todo) VALUES (%s)", (todo,))
    connection.commit()
    cursor.close()
    connection.close()
    return "Todo added", 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    cursor.execute("UPDATE todos SET done = TRUE WHERE id = %s",(todo_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return "Todo updated", 200

@app.route("/healthz")
def health():
    if not is_healthy:
        return "Unhealthy", 500
    try:
        connection = psycopg2.connect(database_url)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        connection.close()
        return "Ok", 200
    except psycopg2.Error:
        return "Can't connect to database", 500

@app.route("/break", methods=["POST"])
def break_app():
    global is_healthy
    is_healthy = False
    return "App broken", 200

if __name__ == "__main__":
    init_db()
    port = int(os.environ["PORT"])
    app.run(host="0.0.0.0", port=port)
