from datetime import datetime, timezone
from beanie import Document, PydanticObjectId
from pydantic import Field


class Goals(Document):
    user_id:PydanticObjectId
    name: str
    target_amount: int
    saved_amount: int 
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Settings: 
    name = "goals"