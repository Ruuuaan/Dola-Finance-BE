from pydantic import BaseModel, ConfigDict
from datetime import datetime
from beanie import PydanticObjectId


class read_user(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: PydanticObjectId
    user_name:str
    email:str
    password_hash: str
    weekly_report: bool=True
    budget_alert:bool 
    created_at:datetime


