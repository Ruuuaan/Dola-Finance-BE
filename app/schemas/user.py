from pydantic import BaseModel, ConfigDict
from datetime import datetime
from beanie import PydanticObjectId
from typing import Literal, Optional

class read_user(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: PydanticObjectId
    username:str
    email:str
    password_hash: str
    weekly_report:bool=True
    budget_alert:bool = True
    created_at:datetime

    


class update_user_settings(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:PydanticObjectId
    name: str
    email: str
    currency: Literal["USD", "PHP"] = "PHP" # set as defaulit 
    monthly_budget: int
    


