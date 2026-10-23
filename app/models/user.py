from datetime import datetime, timezone
from beanie import Document
from typing import Literal
from pydantic import Field
from typing import Optional
from beanie import PydanticObjectId


class UserModel(Document):    
    username:str 
    email: Optional[str]
    password_hash:str
    currency:Literal["USD", "PHP"] = "PHP" #sets default value to PHP
    monthly_budget: Optional[int] = None
    weekly_report: bool = True #sets weekly_reports ON by default 
    budget_alerts: bool = True #sets budget_alerts ON by default
    created_at: datetime = Field(default_factory=lambda:datetime.now(timezone.utc))

class Settings:
    name="users"
