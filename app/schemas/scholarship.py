from pydantic import BaseModel
from typing import List, Optional

class ScholarshipCreate(BaseModel):
    token: str
    name: str
    provider: str
    description: Optional[str] = None
    min_income: Optional[float] = None
    max_income: Optional[float] = None
    min_cgpa: Optional[float] = None
    categories: List[str]
    states: List[str]
