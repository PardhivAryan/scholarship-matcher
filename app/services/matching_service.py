from typing import List

from app.models.user import User
from app.models.scholarship import Scholarship

def _split_csv(value: str) -> List[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]

def calculate_match_score(student: User, scholarship: Scholarship) -> int:
    score = 0

    eligible_states = _split_csv(scholarship.eligible_states)
    eligible_categories = _split_csv(scholarship.eligible_categories)

    if student.state and student.state in eligible_states:
        score += 10
    if student.category and student.category in eligible_categories:
        score += 20
    if student.cgpa is not None and scholarship.min_cgpa is not None:
        if student.cgpa >= scholarship.min_cgpa:
            score += 30
    if student.income is not None and scholarship.max_income is not None:
        if student.income <= scholarship.max_income:
            score += 40

    return score
