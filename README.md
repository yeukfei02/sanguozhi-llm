# sanguozhi-llm

sanguozhi-llm

This project aims to generate text using the `Ollama Llama 3` model with integrated embeddings and a vector database.

Models and Tools:

LLM Model: `digimonster/llama3-chinese-response`
Purpose: Generates responses in Chinese characters.

Embedding Model: `shaw/dmeta-embedding-zh`
Purpose: Provides Chinese character embeddings.

Vector Database: `chromadb`
Description: An AI-native, open-source vector database for efficient data retrieval and storage.

documentation: <https://documenter.getpostman.com/view/3827865/2sAXjF7Zxn>

api url: <>

## Requirement

- install python (v3.12)
- install ollama llama (v3.1)

## Testing and run

```zsh
// install dependencies
$ pip install -r requirements.txt

// pull llm model
$ ollama pull digimonster/llama3-chinese-response

// pull embedding model
$ ollama pull shaw/dmeta-embedding-zh

// run in dev
$ fastapi dev main.py

// run in prod
$ fastapi run main.py
```

```zsh
// install dependencies
$ cd web
$ pip install -r requirements.txt

// open sanguozhi_llm web
$ streamlit run sanguozhi_llm.py
```
