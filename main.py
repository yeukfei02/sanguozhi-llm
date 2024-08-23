from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bacinet import BacinetMiddleware
from src.ollama.sanguozhi_ollama import sanguozhi_ollama
from src.routes.routes import data_router

chroma_sqlite_file = Path("src/ollama/db/chroma.sqlite3")
if not chroma_sqlite_file.is_file():
    # sanguozhi ollama
    sanguozhi_ollama()

app = FastAPI()

# middleware

# cors
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# helmet
app.add_middleware(BacinetMiddleware)

# routes
app.include_router(data_router)
