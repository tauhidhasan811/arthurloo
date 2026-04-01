from dotenv import load_dotenv
from src.services.workflow_executer import WorkFlowExecuter

load_dotenv()

exe = WorkFlowExecuter()
data = exe.check_workflow_status(run_id="69cba338e44d450058289b6e")

print(data.json())
# wrk_data = WorkFlowData()

"""Run a workflow with personality and interest data"""
# text = ""

# with open('data.txt', 'r', encoding="utf-8") as f:
#     for line in f:
#         text+=line
# run_id = wrk_data.run_workflow("personality_and_interest", personality_and_interest_data = text)
# print(run_id)

# return id ->  69cba338e44d450058289b6e

