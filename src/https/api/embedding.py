from fastapi import APIRouter
from src.services import embedding
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/embedding", tags=["embedding"])

@router.post("/")
async def create_embedding(text:str):
    vector = await embedding.create_embedding(text)
    return JSONResponse(status_code=201, content={"embedding": vector})

