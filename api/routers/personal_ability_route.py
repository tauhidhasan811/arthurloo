from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.schemas.personal_ability import PersonalAbility
from src.services.workflow_executer import WorkFlowExecuter


router = APIRouter(prefix="/api/ai/v1/workflow/run", tags=["Personal Ability"])
executer = WorkFlowExecuter()

@router.post("/personal_ability")
async def run_personal_ability(body: PersonalAbility):
    try:
        status, data = executer.run_workflow("personal_ability", body.dict())
        if status:
            response = JSONResponse(
                status_code=200,
                content={
                    "status" : status,
                    "status_code": 200,
                    "run_id": data
                    }
                )
        else:
            response = JSONResponse(
            status_code=500,
            content={
                "status" : status,
                "status_code": 500,
                "message": data
                }
            )
        return response
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "status_code": 500,
                "message": str(e)
                }
            )