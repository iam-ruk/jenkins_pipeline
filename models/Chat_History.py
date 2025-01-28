from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class ChatHistory (SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    user_id: str = Field(nullable=False)
    query: str = Field(nullable=False)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=False)