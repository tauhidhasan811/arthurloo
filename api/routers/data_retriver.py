from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.schemas.learning_style import LearningStyle
from src.services.workflow_executer import WorkFlowExecuter


router = APIRouter(prefix="/api/ai/v1/workflow/retrive-data", tags=["Data Retriver"])
executer = WorkFlowExecuter()

@router.get("/report/{run_id}")
async def run_learning_style(run_id: str):
    try:
        status, data = executer.retrive_workflow_result(run_id=run_id)
        if status:
            response = JSONResponse(
                status_code=200,
                content={
                    "status" : status,
                    "status_code": 200,
                    "data": data
                }
            )

        else:
            response = JSONResponse(
            status_code=200,
            content={
                "status" : status,
                "status_code": 200,
                "data": data
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