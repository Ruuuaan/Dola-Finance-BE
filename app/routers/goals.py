from fastapi import APIRouter, Depends, HTTPException
from app.schemas.goal import Read_Goal,Delete_Goal,UserGoals
from app.models.goal import GoalModel
from app.models.user import UserModel
from datetime import datetime
from beanie import PydanticObjectId
from typing import List



name = __name__.rsplit(".", 1)[-1]
router = APIRouter(prefix="/goal", tags=["Goals"])

@router.post("/create", response_model=Read_Goal)
async def create_goal(
    goal_name:str,
    target_amount:int,
    target_date:datetime
) -> dict:
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
@router.get("/", response_model = UserGoals)
async def get_goal_records(
    user_id:PydanticObjectId
    ):
    try:
        #fetch the user info
        user_data = await UserModel.get(user_id)
        if not user_data:
            raise HTTPException(status_code=404, detail="user with this goal is not found")
        #fetching goals that is inside the current user?
        user_goals = await GoalModel.find(
        GoalModel.user_id == user_id).to_list()

        response_data={
            "user_id": user_data.id,
            "username": user_data.username,
            "goals":user_goals
                
        }
        return response_data
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





    


  
