from fastapi import APIRouter
from fastapi.responses import JSONResponse
from https.request.text import TextRequest
from services.tag import create_tag

router = APIRouter(prefix="/tag", tags=["tag"])

@router.post("/")
async def generate_tags(req: TextRequest):
    
    tags = await create_tag(req.text)
    return JSONResponse(status_code=201, content={"tags": tags})