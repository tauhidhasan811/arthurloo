from src.hyper_params import params
from src.config.workflow_data import WorkFlowData

class WorkFlowExecuter:
    def __init__(self):
        self.wrk_data = WorkFlowData()
    
    def run_workflow(self, workflow_name, **kwargs):

        service = params["workflow_service"]["run"]
        data = params["workflow_list"][workflow_name]
        url = service['url'] + data['id']


        # response = response.json()
        # #output ----> {'message': 'Successfully triggered workflow run', 'workflow_run_id': '69ca55977861951155e0b53e'}
        # if response['message'] == "Successfully triggered workflow run":
        #     return response['workflow_run_id']
        # else:
        #     return "Failed to run workflow"