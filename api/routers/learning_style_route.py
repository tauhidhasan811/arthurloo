from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.schemas.learning_style import LearningStyle
from src.services.workflow_executer import WorkFlowExecuter


router = APIRouter(prefix="/api/ai/v1/workflow/run", tags=["Learning style"])
executer = WorkFlowExecuter()

@router.post("/learning_style")
async def run_learning_style(body: LearningStyle):
    try:
        status, data = executer.run_workflow("learning_style", body.dict())
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