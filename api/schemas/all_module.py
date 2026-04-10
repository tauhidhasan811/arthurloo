from pydantic import BaseModel
from typing import Dict

class AllModuleData(BaseModel):
    personality_and_interest_data: Dict
    learning_style_data: Dict
    personal_ability_data: Dict
