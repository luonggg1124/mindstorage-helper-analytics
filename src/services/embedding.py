
from fastembed import TextEmbedding

model = TextEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

async def create_embedding(text: str) -> list[float]:
    vector = next(model.embed([text]))
    return vector.tolist()