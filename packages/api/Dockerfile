FROM --platform=linux/amd64 python:3.12-slim

RUN mkdir -p /app

WORKDIR /app

COPY ./ .

RUN apt-get update && apt-get install -y curl

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN sh /app/run-ollama.sh

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]