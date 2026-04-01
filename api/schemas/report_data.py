from pydantic import BaseModel

class ReportBody(BaseModel):
    personality_and_interest_data: str
    learning_style_data:  str
    personal_ability_data: str