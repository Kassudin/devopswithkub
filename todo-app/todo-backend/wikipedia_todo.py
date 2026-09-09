import os
import json
import urllib.request

wikipedia_url = os.environ["WIKIPEDIA_URL"]
backend_url = os.environ["BACKEND_URL"]

# Without this Wikipedia will return 403 Forbidden t: chat-gpt
request = urllib.request.Request(
    wikipedia_url,
    headers={"User-Agent": "todo-app"}
)

with urllib.request.urlopen(request) as response:
    article_url = response.geturl()
data = json.dumps({"todo": f"read {article_url}"}).encode()

request = urllib.request.Request(
    backend_url,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

urllib.request.urlopen(request)
