from  fastapi import APIRouter,HTTPException
from app.schemas.user import read_user, update_user_settings
from app.models.user import UserModel
from beanie import PydanticObjectId
from datetime import datetime
from typing import List

name = __name__.rsplit(".", 1)[-1]
router = APIRouter(prefix="/user", tags=["User"])

@router.post("/create", response_model=read_user)
async def create_user(username:str, email:str, password:str)-> dict:
    try:
        user=UserModel(
        username=username,
        email=email,
        password_hash=password
        )
        await user.create()
        return user
    except Exception as e: 
        raise HTTPException (status_code=500, detail=str(e))

@router.get("/get user", response_model=read_user)
async def get_user_info(id:PydanticObjectId)->dict:
    try:
        return await UserModel.get(id)
    except Exception as e: 
        raise HTTPException(status_code=500, detail=str(e))







