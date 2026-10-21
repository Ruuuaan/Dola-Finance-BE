from fastapi import APIRouter, Depends, HTTPException
from app.schemas.goal import Read_Goal,Delete_Goal
from app.models.goal import GoalModel
from datetime import datetime
from beanie import PydanticObjectId
from typing import List



name = __name__.rsplit(".", 1)[-1]
router = APIRouter(prefix="/goal", tags=["Goals"])

@router.post("/create", response_model=Read_Goal)
async def create_goal(goal_name:str,target_amount:int, target_date:datetime) -> dict:
    try:
        goal = GoalModel (
        user_id = PydanticObjectId(),
        goal_name = goal_name,
        target_amount=target_amount,
        target_date=target_date
        )
        await goal.create()
        return goal
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""@router.put("/{id}")
async def update_goal(id: PydanticObjectId, user_id:int,):
    try:

        return goal
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
"""
@router.get("/", response_model = List[Read_Goal])
async def get_goal_records():
    try:
        return await GoalModel.find_all().to_list()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.delete("/", response_model=dict)
async def delete_goal(
    id: PydanticObjectId
):
    try:
        # fetch before deleting
        goal = await GoalModel.get(id)
        if not goal:
        #check if goal is there 
            raise HTTPException(status_code=404, detail="Goal not found")
        await goal.delete()

        #delete goal from db 
        return {"message": "Goal successfully deleted"}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





    


  
