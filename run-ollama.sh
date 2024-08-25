#! /bin/zsh

ollama serve &
ollama list
ollama pull digimonster/llama3-chinese-response

ollama serve &
ollama list
ollama pull shaw/dmeta-embedding-zh