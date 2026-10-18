from typing import Literal, Optional
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/analytics", tags=["Analytics"])


"""
@router.get("/summary")
async def analytics_summary():
    try:
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="failed to get analytic summary")"""



    
"""
@router.get("/insights")
async def analytics_insights():
    try:

    except Exception as e: 
        raise HTTPException(status_code=500, detail="failed to fetch analytic insight")"""

