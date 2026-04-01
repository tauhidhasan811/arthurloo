from pydantic import BaseModel, model_validator
from src.hyper_params import params
class ReportBody(BaseModel):
    report_name: str
    personality_and_interest_data: str
    learning_style_data:  str
    personal_ability_data: str


    @model_validator(mode="after")
    def validate_report_name(self):
        if self.report_name not in params['reports']:
            raise ValueError(f"Invalid report name. Must be one of {params['reports']}")
        return self