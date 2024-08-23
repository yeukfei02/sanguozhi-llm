FROM --platform=linux/amd64 python:3.12-slim

RUN mkdir -p /app

WORKDIR /app

COPY ./ .

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN ollama pull digimonster/llama3-chinese-response

RUN ollama pull shaw/dmeta-embedding-zh

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]