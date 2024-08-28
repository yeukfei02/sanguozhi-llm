#! /bin/zsh

ollama serve &
ollama pull digimonster/llama3-chinese-response
ollama pull shaw/dmeta-embedding-zh
ollama list