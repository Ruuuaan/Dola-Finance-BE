from datetime import datetime, timezone
from beanie import Document, PydanticObjectId
from typing import Literal
from pydantic import Field


class Transaction(Document):
    user_id: PydanticObjectId
    category_id: PydanticObjectId
    merchant: str
    amount: int
    transaction_type: Literal["income","expense"] #sets what the type of transaction is seen on the transaction details
    date: datetime = Field(default_factory=lambda:datetime.now(timezone.utc))
    created_at: datetime= Field(default_factory=lambda: datetime.now(timezone.utc))

class Settings:
    name = "transactions"