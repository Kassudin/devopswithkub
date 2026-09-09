import os

import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

database_url = os.environ["DATABASE_URL"]

def init_db():
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            todo TEXT NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()

@app.route("/todos", methods=["GET"])
def get_todos():
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()

    cursor.execute("SELECT todo FROM todos ORDER BY id")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    todos = [row[0] for row in rows]
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    todo = data["todo"]
    if len (todo) > 140:
        return "Maximum length of todo is 140", 400
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO todos (todo) VALUES (%s)", (todo,))
    connection.commit()
    cursor.close()
    connection.close()
    return "Todo added", 201

if __name__ == "__main__":
    init_db()
    port = int(os.environ["PORT"])
    app.run(host="0.0.0.0", port=port)