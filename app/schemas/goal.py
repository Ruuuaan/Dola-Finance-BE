from pydantic import BaseModel,ConfigDict
from beanie import PydanticObjectId
from datetime import datetime 


class Read_Goal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id :PydanticObjectId
    goal_name: str
    target_amount:int
    target_date: datetime
    created_at: datetime 

