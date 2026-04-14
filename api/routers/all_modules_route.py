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
        personality_and_interest_data = module_data.personality_and_interest_data
        learning_style_data = module_data.learning_style_data
        personal_ability_data = module_data.personal_ability_data

        PI_status, PI_run_id = executer.run_workflow("personality_and_interest", personality_and_interest_data)
        LS_status, LS_run_id = executer.run_workflow("learning_style", learning_style_data)
        PA_status, PA_run_id = executer.run_workflow("personal_ability", personal_ability_data)

        status = False
        if PI_status and LS_status and PA_status:
            status = True
        run_ids.extend([
            {'personality_and_interest': PI_run_id}, 
            {'learning_style': LS_run_id}, 
            {'personal_ability': PA_run_id}
            ])
        
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