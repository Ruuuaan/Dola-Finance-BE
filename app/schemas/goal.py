from pydantic import BaseModel,ConfigDict
from beanie import PydanticObjectId
from datetime import datetime 
from typing import Optional, List


class Read_Goal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id :PydanticObjectId
    goal_name:str
    target_amount:int
    saved_amount:int
    target_date: datetime
    created_at: datetime 

class UserGoals(BaseModel):
    user_id:PydanticObjectId
    username:str
    goals: List[Read_Goal]

class Delete_Goal(BaseModel):
    id: PydanticObjectId
    message: Optional[str]

class Update_Goal(BaseModel):
    goal_name:str
    target_amount:int
    saved_amount:int
    target_date:datetime