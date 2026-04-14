# from dotenv import load_dotenv
# from src.services.workflow_executer import WorkFlowExecuter

# load_dotenv()

# exe = WorkFlowExecuter()
# data = exe.retrive_workflow_result(run_id="69cba338e44d450058289b6e")

# print(data)
# # wrk_data = WorkFlowData()

# """Run a workflow with personality and interest data"""
# # text = ""

# # with open('data.txt', 'r', encoding="utf-8") as f:
# #     for line in f:
# #         text+=line
# # run_id = wrk_data.run_workflow("personality_and_interest", personality_and_interest_data = text)
# # print(run_id)

# # return id ->  69cba338e44d450058289b6e


from fastapi import FastAPI, exception_handlers, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from api.routers.personality_and_interest_route import router as personality_and_interest_router
from api.routers.learning_style_route import router as learning_style_router
from api.routers.personal_ability_route import router as personal_ability_router
from api.routers.all_modules_route import router as all_module_router
from api.routers.report_router import router as report_router
from api.routers.data_retriver import router as data_retriver_route



app = FastAPI(title="Workflow API", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc: RequestValidationError):
#     message = "Validation errors:"
#     for error in exc.errors():
#         message += f"\nField: {error['loc']}, Error: {error['msg']}"
#     return JSONResponse(
#         status_code=400,
#         content={
#             "status_code":400,
#             "data": message
#             }
#     )


@app.get('/', tags=['Helth check'])
async def health_check():
    return JSONResponse(
        status_code=200,
        content={
            'status': True,
            'status_code': 200,
            'response': "Helth check"
        }
    )



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # print(exc.errors())
    error_msg = exc.errors()[0]['msg']

    return JSONResponse(
        status_code=400,
        content={
            "status": False,
            "status_code": 400,
            "message": error_msg
        },
    )




app.include_router(personality_and_interest_router)
app.include_router(learning_style_router)
app.include_router(personal_ability_router)
app.include_router(all_module_router)
app.include_router(report_router)
app.include_router(data_retriver_route)

