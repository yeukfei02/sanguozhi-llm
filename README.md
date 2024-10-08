# sanguozhi-llm

sanguozhi-llm

Data source: `三國志`, `三國演義`, `三國志十遊戲`

This project aims to generate text using the `Ollama Llama 3` model with integrated embeddings and a vector database.

Models and Tools:

LLM Model: `digimonster/llama3-chinese-response`

Purpose: Generates responses in Chinese characters.

Embedding Model: `shaw/dmeta-embedding-zh`

Purpose: Provides Chinese character embeddings.

Vector Database: `chromadb`

Description: An AI-native, open-source vector database for efficient data retrieval and storage.

documentation: <https://documenter.getpostman.com/view/3827865/2sAXjF7Zxn>

api url: <http://localhost:8000>

web url: <http://localhost:8501>

## Requirement

- install python (v3.12)
- install ollama llama (v3)

## Testing and run

```zsh
// install dependencies
$ cd packages/api
$ pip install -r requirements.txt

// pull llm model
$ ollama pull digimonster/llama3-chinese-response

// pull embedding model
$ ollama pull shaw/dmeta-embedding-zh

// seed chromadb
$ cd packages/api
$ python seed_chromadb.py

// run ollama
$ cd packages/api
$ sh run-ollama.sh

// run in dev
$ cd packages/api
$ fastapi dev main.py

// run in prod
$ cd packages/api
$ fastapi run main.py
or
$ uvicorn main:app --host 0.0.0.0 --port 80
```

```zsh
// install dependencies
$ cd packages/web
$ pip install -r requirements.txt

// open sanguozhi_llm web
$ streamlit run sanguozhi_llm.py
```
