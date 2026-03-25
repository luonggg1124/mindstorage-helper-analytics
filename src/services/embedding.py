
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
async def create_embedding(text:str)->list[float] :
    vector = await model.encode(text)
    return vector.tolist()