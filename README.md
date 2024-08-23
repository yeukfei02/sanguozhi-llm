# sanguozhi-llm

sanguozhi-llm

## Requirement

- install python (v3.12)
- install ollama llama (v3.1)

## Testing and run

```zsh
// install node dependencies
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
