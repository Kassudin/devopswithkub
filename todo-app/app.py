import os
import time
import urllib.request

from flask import Flask, send_file


app = Flask(__name__)

image_url = "https://picsum.photos/1200"
image_file = "/usr/src/app/files/image.jpg"

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

@app.route("/todo")
def index():
    return """
    <h1>Todo app</h1>
    <img src="/todo/image" width="600" alt="Random image">
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
