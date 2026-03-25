from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.chat import handle_chat
router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/")
async def chat():
    answer = await handle_chat()
    return JSONResponse(status_code=201, content={"answer": answer})