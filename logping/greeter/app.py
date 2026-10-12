from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return os.getenv("GREETING", "sup")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
