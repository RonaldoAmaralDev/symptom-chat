FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev python3-opencv && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

WORKDIR /app/api

EXPOSE 8088

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]