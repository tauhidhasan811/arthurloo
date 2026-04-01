from src.hyper_params import params
from src.config.workflow_data import WorkFlowData

class WorkFlowExecuter:
    def __init__(self):
        self.wrk_data = WorkFlowData()
    
    def run_workflow(self, workflow_name, **kwargs):

        service = params["workflow_service"]["run"]
        data = params["workflow_list"][workflow_name]
        url = service['url'] + data['id']

        response = self.wrk_data.execute_workflow(method=service['method'], url=url, data=kwargs)
        if response['message'] == "Successfully triggered workflow run":
            return response['workflow_run_id']
        else:
            return "Failed to run workflow"
        #output ----> {'message': 'Successfully triggered workflow run', 'workflow_run_id': '69ca55977861951155e0b53e'}
        if response['message'] == "Successfully triggered workflow run":
            return response['workflow_run_id']
        else:
            return "Failed to run workflow"
        
    def check_workflow_status(self, run_id):
        service = params['workflow_service']["status"]
        url = service['url'] + run_id
        response = self.wrk_data.execute_workflow(method=service['method'], url=url)

        # output --->  {'workflow_run_id': '69cba338e44d450058289b6e', 'status': 'COMPLETED'}
        return response
    
    def retrive_workflow_result(self, run_id):
        service = params['workflow_service']["result"]
        url = service['url'] + run_id
        response = self.wrk_data.execute_workflow(method=service['method'], url=url)
        """
        output ---> {
            'workflow_run_id': '69cba338e44d450058289b6e', 
            'workflow_id': '69cb3e0c6b30038ca03a1b90', 
            'workflow_title': '3. Class Individual Ability Assessment', 
            'workflow_run_input': [{'title': 'personal_ability_data', 'type': 'TEXT', 'content': '', 'index': 0}], 
            'workflow_run_output': [{'index': 0, 'title': 'Developmental Analysis', 'type': 'AGENT', 'content': '.....................AI response'}
                                     ]
            }
        """
        return response['workflow_run_output'][0]['content']