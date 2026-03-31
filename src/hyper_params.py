import os
from dotenv import load_dotenv
load_dotenv()


headers = {
    "accept": "application/json",
    "x-api-key": os.environ.get("MINDPAL_API_KEY"),
    "Content-Type": "application/json"
}

params = {
    "workflow_id": ["69ca4c4689c6022432b26c89"],
    "workflow_base_url": {
        "run": "https://api.mindpal.io/api/v2/workflow/run?workflow_id=",
        
    }
}
