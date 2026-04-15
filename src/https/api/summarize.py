from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..request.text import TextRequest
from ...services.summarize import summarize_text

router = APIRouter(prefix="/summarize", tags=["summarize"])

@router.post("")
async def summarize(req: TextRequest):
    summary = await summarize_text(req.text)
    return JSONResponse(status_code=201, content={"summary": summary})