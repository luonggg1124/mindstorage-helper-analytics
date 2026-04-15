
from .ollama_ai_model import ask_ollama




async def summarize_text(text:str):
    prompt = prompt = f"""
    Summarize the following note in 3 bullet points:
    {text}
    """
    summary = await ask_ollama(prompt)
    return summary