from pydantic import BaseModel, ConfigDict
from beanie import PydanticObjectId
from datetime import datetime
from typing import Literal


class ReadTransaction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:PydanticObjectId
    transaction_name:str
    merchant_name:str
    transaction_type: Literal["income", "expense"]
    date:datetime
    created_at:datetime

