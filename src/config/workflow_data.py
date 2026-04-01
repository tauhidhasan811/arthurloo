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
            
        elif method =="GET":
            response = requests.get(url, headers=self.headers)
            
        else: 
            raise ValueError("Unsupported HTTP method")
        return response.json()

    