from src.hyper_params import params
from src.config.config_executer import ConfigExecuter

class WorkFlowExecuter:
    def __init__(self):
        self.wrk_executer = ConfigExecuter()
    
    def run_workflow(self, workflow_name, body_data: dict):
        
        service = params["workflow_service"]["run"]
        data = params["workflow_list"][workflow_name]
        url = service['url'] + data['id']

        response = self.wrk_executer.execute_workflow(method=service['method'], url=url, body=body_data)
        # print(response)
        status = response['success']
        if status:
            return status, response['workflow_run_id']

        return status, "Failed to run workflow"
        #output ----> {'success': True, 'status_code': 200, 'message': 'Successfully triggered workflow run', 'workflow_run_id': '69d9a69e263277d9bd508c25'}
        
        
    def check_workflow_status(self, run_id):
        service = params['workflow_service']["status"]
        url = service['url'] + run_id
        response = self.wrk_executer.execute_workflow(method=service['method'], url=url)
        status = response.get("status")
        if status == 'COMPLETED':
            return True
        return False
        # output --->  {'workflow_run_id': '69cba338e44d450058289b6e', 'status': 'COMPLETED'}
        # return response
    
    def retrive_workflow_result(self, run_id):
        service = params['workflow_service']["result"]
        url = service['url'] + run_id
        response = self.wrk_executer.execute_workflow(method=service['method'], url=url)
        """
        output ---> {
            'workflow_run_id': '69cba338e44d450058289b6e', 
            'workflow_id': '69cb3e0c6b30038ca03a1b90', 
            'workflow_title': '3. Class Individual Ability Assessment', 
            'workflow_run_input': [{'title': 'personal_ability_data', 'type': 'TEXT', 'content': '', 'index': 0}], 
            'workflow_run_output': [
                                        {
                                            'index': 0, 
                                            'title': 'Developmental Analysis',
                                            'type': 'AGENT', 
                                            'content': '.....................AI response'
                                        }
                                     ]
            }
        """
        if response['workflow_run_id'] == run_id:
            status = True
            content = response['workflow_run_output'][0]['content']
        else:
            status = False
            content = "No data found"
        return status, content