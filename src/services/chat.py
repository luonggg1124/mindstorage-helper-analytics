
from .ollama_ai_model import ask_ollama

async def handle_chat(question: str, context: list[str] | None = None) -> str:
    cont = ""
    if context:
        cont = "\n".join(context)
    prompt = f"""
    Context:
    {cont}

    Question:
    {question}

    Answer clearly.
    """
    answer = await ask_ollama(prompt)
    return answer