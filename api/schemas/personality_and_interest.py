from pydantic import BaseModel
from typing import Dict

class PersonalityAndInterest(BaseModel):
    personality_and_interest_data: Dict
