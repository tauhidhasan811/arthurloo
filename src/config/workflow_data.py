import requests
from src.hyper_params import headers, params

class WorkFlowData:
    def __init__(self):
        self.headers= headers
    
    def run_workflow(self, task, workflow_name, input_data: None):
        workflow_data = params["workflow"]["run"]
        workflow_id = params["workflow_list"][workflow_name]
        url = workflow_data['url'] + workflow_id
        method = workflow_data['method']
        if method == "POST":
            response = requests.post(url, headers=self.headers, json=input_data)
        elif method =="GET":
            response = requests.get(url, headers=self.headers)
        else: 
            raise ValueError("Unsupported HTTP method")
        return response.json()