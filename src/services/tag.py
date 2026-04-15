from .ollama_ai_model import ask_ollama

async def create_tag(text:str) -> list[str]: 
    prompt = f"""
    Extract 5 tags from the note.

    Note:
    {text}

    Return comma separated tags.
    """
    result = await ask_ollama(prompt)
    tags = result.split(",")
    return tags