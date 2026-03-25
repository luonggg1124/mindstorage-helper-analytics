from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.services import summarize

router = APIRouter(prefix="/summarize", tags=["summarize"])


@router.post("/")
async def summarize_text(text: str):
    summary = await summarize.summarize_text(text)
    return JSONResponse(status_code=201, content={"summary": summary})