from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..request.chat import ChatRequest
from ...services.chat import handle_chat

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("")
async def chat(req: ChatRequest):
    answer = await handle_chat(req.question, req.context)
    return JSONResponse(status_code=201, content={"answer": answer})