from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    question: str
    context: Optional[List[str]] = None