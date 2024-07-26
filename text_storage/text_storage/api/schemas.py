from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TextFragmentSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str
    author: str
    source: str
    tags: list[str]


class TextFragmentResponseSchema(BaseModel):
    id: UUID
    text: str
    author: str
    source: str
    tags: list[str]
    created_at: datetime
