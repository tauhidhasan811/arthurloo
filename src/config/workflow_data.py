import requests
from src.hyper_params import headers, params

class WorkFlowData:
    def __init__(self):
        self.headers= headers
    
    def execute_workflow(self, method, url, data: dict=None):
        
        # service = params["workflow_service"][service_type]
        # url = service['url'] + id
        if method == "POST":
            response = requests.post(url, headers=self.headers, json=data)
            if response['message'] == "Successfully triggered workflow run":
                return response['workflow_run_id']
            else:
                return "Failed to run workflow"
        elif method =="GET":
            response = requests.get(url, headers=self.headers)
            return response
        else: 
            raise ValueError("Unsupported HTTP method")
        

    