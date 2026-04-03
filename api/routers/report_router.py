from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.schemas.report_data import ReportBody
# from src.services.workflow_executer import WorkFlowExecuter
from src.services.report_processor import ReportProcessor


router = APIRouter(prefix="/api/ai/v1/workflow/run", tags=["Report generator"])
processor = ReportProcessor()

@router.post("/report")
async def run_report(body: ReportBody):
    try:
        # report_name = body.report_name
        # # print(body.dict())
        # body_data = body.dict()
        # body_data.pop("report_name")
        # return body_data
        status, response_data = processor.process_report(body)
        # status = True
        # status, data = executer.run_workflow(report_name, body_data)
        if status:
            response = JSONResponse(
                status_code=200,
                content={
                    "status" : status,
                    "status_code": 200,
                    "run_id": response_data
                    }
                )
            
        else:
            response = JSONResponse(
            status_code=200,
            content={
                "status" : status,
                "status_code": 200,
                "message": response_data
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