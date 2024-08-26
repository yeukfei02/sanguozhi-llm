from pathlib import Path
from ollama_llm.sanguozhi_ollama import sanguozhi_ollama

chroma_sqlite_file = Path("ollama_llm/db/chroma.sqlite3")
if not chroma_sqlite_file.is_file():
    # sanguozhi ollama
    sanguozhi_ollama()
    print("seed chromadb success")
else:
    print("chromadb already exists")
