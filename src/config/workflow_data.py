import requests
from src.hyper_params import headers, params

class WorkFlowData:
    def __init__(self):
        self.headers= headers
    
    def execute_workflow(self, method, url, body: dict=None):
        if method == "POST":
            response = requests.post(url, headers=self.headers, json=body)
        elif method =="GET":
            response = requests.get(url, headers=self.headers)
        else: 
            raise ValueError("Unsupported HTTP method")
        return response.json()

    