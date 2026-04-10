from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.schemas.all_module import AllModuleData
from src.services.workflow_executer import WorkFlowExecuter
router = APIRouter(prefix='/api/ai/v1/workflow/run', tags=["All module"])

executer = WorkFlowExecuter()
@router.post('/all-module/')
async def run_all_module(module_data: AllModuleData):
    try:
        run_ids = []
        personality_and_interest_data = module_data.get("personality_and_interest", "")
        learning_style_data = module_data.get("learning_style", "")
        personal_ability_data = module_data.get("personal_ability", "")

        PI_status, PI_run_id = executer.run_workflow("personality_and_interest", personality_and_interest_data.dict())
        LS_status, LS_run_id = executer.run_workflow("learning_style", learning_style_data.dict())
        PA_status, PA_run_id = executer.run_workflow("personal_ability", personal_ability_data.dict())

        status = False
        if PI_status and LS_status and PA_status:
            status = True
        run_ids.extend([PI_run_id, LS_run_id, PA_run_id])
        
        if status:
            response = JSONResponse(
                status_code=200,
                content={
                    "status" : status,
                    "status_code": 200,
                    "run_id": run_ids
                    }
                )
        else:
            response = JSONResponse(
            status_code=500,
            content={
                "status" : status,
                "status_code": 500,
                "message": run_ids
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