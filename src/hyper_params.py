import os
from dotenv import load_dotenv
load_dotenv()


headers = {
    "accept": "application/json",
    "x-api-key": os.environ.get("MINDPAL_API_KEY"),
    "Content-Type": "application/json"
}

params = {
    "workflow_list": {
        "personality_and_interest": "69cb3e0c6b30038ca03a1b90",
        "learning_style": "69cb3a136b30038ca03a1b65",
        "personal_ability": "69ca4c4689c6022432b26c89",
        "idp": "69cb4e9b234d4920c169871c",
        "idp-pd": "69cb5159234d4920c1698738",
        "ifp": "69cb568ca66602ff1552139a",
        "ifp-pd": "69cb6777289bc826a836fdf5"
    },
    "workflow": {
        "run": {
            "url": "https://api.mindpal.io/api/v2/workflow/run?workflow_id=",
            "method": "POST"
        },
        "status": {
            "url": "https://api.mindpal.io/api/workflow-run-status/retrieve-by-id?run_id=",
            "method": "GET"
        },
        "result": {
            "url": "https://api.mindpal.io/api/workflow-run-result/retrieve-by-id?run_id=",
            "method": "GET"
        }
    }
}
