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
        "personality_and_interest": {
            "id": "69cb3e0c6b30038ca03a1b90",
            "input_variables" : ["personality_and_interest_data"]
        },
        "learning_style": {
            "id": "69cb3a136b30038ca03a1b65",
            "input_variables" : [ "learning_style_data"]
        },
        "personal_ability": {
            "id": "69cb3e0c6b30038ca03a1b90",
            "input_variables": ["personal_ability_data"]
        },
        "idp": {
            "id": "69cb4e9b234d4920c169871c",
            "input_variables": ["personality_and_interest_data", "learning_style_data", "personal_ability_data"]
        },
        "idp-pd": {
            "id": "69cb5159234d4920c1698738",
            "input_variables": ["personality_and_interest_data", "learning_style_data", "personal_ability_data"]
        },
        "ifp": {
            "id": "69cb568ca66602ff1552139a",
            "input_variables": ["personality_and_interest_data", "learning_style_data", "personal_ability_data"]
        },
        "ifp-pd": {
            "id": "69cb6777289bc826a836fdf5",
            "input_variables": ["personality_and_interest_data", "learning_style_data", "personal_ability_data"]
        }
    },
    "workflow_service": {
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
    },
    'reports' : ["idp", "idp-pd", "ifp", "ifp-pd"]
}
