from src.db_manager.databse_manager import DatabaseManager
from src.services.workflow_executer import WorkFlowExecuter
from api.schemas.report_data import ReportBody

class ReportProcessor:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.workflow_executer = WorkFlowExecuter()
    
    def process_report(self, reportBody: ReportBody):
        print(reportBody.child_id)
        child_data = self.db_manager.get_data(reportBody.child_id)
        print(child_data)
        personality_and_interest_data = child_data.get("personality_and_interest", "")
        learning_style_data = child_data.get("learning_style", "")
        personal_ability_data = child_data.get("personal_ability", "")
        if not personality_and_interest_data :
            return False, "Personality and interest data is required to generate the report."
        if not learning_style_data :
            return False, "Learning style data is required to generate the report."
        if not personal_ability_data:
            return False, "Personal ability data is required to generate the report."
        body_data = {
            "personality_and_interest_data": personality_and_interest_data,
            "learning_style_data": learning_style_data,
            "personal_ability_data": personal_ability_data
        }
        print(body_data)
        status, run_id = self.workflow_executer.run_workflow("report_generation", body_data)

        return status, run_id