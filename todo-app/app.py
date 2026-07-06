import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Todo app"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)

