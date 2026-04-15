
import os
import httpx

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = os.getenv("OLLAMA_MODEL", "llama3")

async def ask_ollama(prompt: str) -> str:
    async with httpx.AsyncClient(timeout=60.0) as client:
        res = await client.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False})
        
        return res.json()["response"]