from beanie import init_beanie
from pymongo import AsyncMongoClient

from app.core.config import settings
from app.models.goal import GoalModel
from app.models.user import UserModel

async def init_db():

    client = AsyncMongoClient(settings.mongodb_uri)
    await init_beanie(
        database =client[settings.database_name],
        document_models =[GoalModel, UserModel]
        
    )