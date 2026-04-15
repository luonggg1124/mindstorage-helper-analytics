from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .https.api.chat import router as chat_router
from .https.api.embedding import router as embedding_router
from .https.api.summarize import router as summarize_router
from .https.api.tag import router as tag_router


app = FastAPI()

# Include API routers with /api prefix
app.include_router(chat_router, prefix="/api", tags=["chat"])
app.include_router(embedding_router, prefix="/api", tags=["embedding"])
app.include_router(summarize_router, prefix="/api", tags=["summarize"])
app.include_router(tag_router, prefix="/api", tags=["tag"])

@app.get("/")
async def root():
    return JSONResponse(status_code=200, content={"message": "Hello, World!"})