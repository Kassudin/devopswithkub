import os
import psycopg2
from flask import Flask

app = Flask(__name__)

database_url = os.environ["DATABASE_URL"]

def init_db():
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pingpong (
    id INTEGER PRIMARY KEY,
    counter INTEGER NOT NULL
    )
    """)
    cursor.execute("""
    Insert INTO pingpong (id, counter)
    VALUES (1, 0) 
    ON CONFLICT (id) DO NOTHING
    """)
    connection.commit()
    cursor.close()
    connection.close()

def get_counter():
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    cursor.execute("""
    SELECT counter
    FROM pingpong
    WHERE id = 1
    """)
    counter = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return counter


@app.route("/")
def pingpong():
    connection = psycopg2.connect(database_url)
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE pingpong
    SET counter = counter + 1
    WHERE id = 1
    RETURNING counter - 1
    """)
    counter = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return f"pong: {counter}"

@app.route("/pings")
def pings():
    return str(get_counter())

@app.route("/healthz")
def health():
    try:
        init_db()
        return "ok", 200
    except psycopg2.OperationalError:
        return "Can't connect database", 500

if __name__ == "__main__":
    try:
        init_db()
    except psycopg2.OperationalError:
        pass
    port = int(os.environ["PORT"])
    app.run(host="0.0.0.0", port=port)
    