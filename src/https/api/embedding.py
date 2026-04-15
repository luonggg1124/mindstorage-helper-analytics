from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..request.text import TextRequest
from ...services.embedding import create_embedding

router = APIRouter(prefix="/embedding", tags=["embedding"])

@router.post("")
async def embedding(req: TextRequest):
    vector = await create_embedding(req.text)
    return JSONResponse(status_code=201, content={"embedding": vector})

