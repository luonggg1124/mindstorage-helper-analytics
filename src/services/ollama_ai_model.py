
import requests



OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def ask_ollama(prompt:str) -> str: 
    res = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False})
    return res.json()["response"]