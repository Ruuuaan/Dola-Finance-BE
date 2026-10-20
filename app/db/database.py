from beanie import init_beanie
from pymongo import AsyncMongoClient

from app.core.config import settings
from app.models.goal import GoalModel

async def init_db():

    client = AsyncMongoClient(settings.mongodb_uri)
    await init_beanie(
        database =client[settings.database_name],
        document_models =[GoalModel]
    )