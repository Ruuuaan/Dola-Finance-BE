from beanie import PydanticObjectId
from pydantic import BaseModel, ConfigDict


class CategoryRead(BaseModel):
    model_config=ConfigDict(from_attributes= True)

    id:PydanticObjectId
    name: str
    