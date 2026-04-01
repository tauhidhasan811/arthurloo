from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.schemas.personality_and_interest import PersonalityAndInterest
from src.services.workflow_executer import WorkFlowExecuter


router = APIRouter(prefix="/api/ai/v1/workflow/run", tags=["Personality and Interest"])
executer = WorkFlowExecuter()

@router.post("/personality_and_interest")
async def run_personality_and_interest(body: PersonalityAndInterest):
    try:
        status, data = executer.run_workflow("personality_and_interest", body.dict())
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