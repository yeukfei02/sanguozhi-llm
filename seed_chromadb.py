from pathlib import Path
from packages.ollama.sanguozhi_ollama import sanguozhi_ollama

chroma_sqlite_file = Path("packages/ollama/db/chroma.sqlite3")
if not chroma_sqlite_file.is_file():
    # sanguozhi ollama
    sanguozhi_ollama()
