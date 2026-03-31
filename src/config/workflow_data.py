import requests
from src.hyper_params import headers, params

class WorkFlowData:
    def __init__(self):
        self.headers= headers
    
    def run_workflow(self, workflow_name, **kwargs):
        service = params["workflow_service"]["run"]
        data = params["workflow_list"][workflow_name]
        url = service['url'] + data['id']

        method = service['method']
        if method == "POST":
            response = requests.post(url, headers=self.headers, json=kwargs)
        elif method =="GET":
            response = requests.get(url, headers=self.headers)
        else: 
            raise ValueError("Unsupported HTTP method")
        response = response.json()
        #output ----> {'message': 'Successfully triggered workflow run', 'workflow_run_id': '69ca55977861951155e0b53e'}
        if response['message'] == "Successfully triggered workflow run":
            return response['workflow_run_id']
        else:
            return "Failed to run workflow"