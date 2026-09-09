FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY todobackend.py .
COPY wikipedia_todo.py .

CMD ["python", "todobackend.py"]
