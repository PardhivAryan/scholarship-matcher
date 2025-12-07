from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.scholarship import Scholarship
from app.models.user import User
from app.services.matching_service import calculate_match_score
from app.services.search_service import search_scholarships
from app.utils.jwt_handler import decode_token
from app.schemas.scholarship import ScholarshipCreate   # <-- IMPORTANT

router = APIRouter(prefix="/scholarships", tags=["Scholarships"])


# -----------------------------
# Helper: Get current user from token
# -----------------------------
def _get_current_user(token: str, db: Session) -> User:
    try:
        payload = decode_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == payload.get("user_id")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# -----------------------------
# Create Scholarship (JSON Body)
# -----------------------------
@router.post("/create")
def create_scholarship(
    data: ScholarshipCreate,      # <-- JSON body instead of query params
    db: Session = Depends(get_db)
):
    # Validate token
    _ = decode_token(data.token)

    # Create scholarship
    new_sch = Scholarship(
        name=data.name,
        provider=data.provider,
        description=data.description,
        min_income=data.min_income,
        max_income=data.max_income,
        min_cgpa=data.min_cgpa,
        # Save lists as comma-separated strings
        eligible_categories=",".join(data.categories),
        eligible_states=",".join(data.states),
    )

    db.add(new_sch)
    db.commit()
    db.refresh(new_sch)

    return {"message": "Scholarship created", "id": new_sch.id}


# -----------------------------
# Search Scholarships
# -----------------------------
@router.get("/search")
def search(query: str):
    return search_scholarships(query)


# -----------------------------
# Match Scholarships to Student
# -----------------------------
@router.get("/match")
def match(
    token: str,
    db: Session = Depends(get_db)
):
    student = _get_current_user(token, db)

    scholarships = db.query(Scholarship).all()
    results = []

    for s in scholarships:
        score = calculate_match_score(student, s)
        sch_data = {
            "id": s.id,
            "name": s.name,
            "provider": s.provider,
            "description": s.description,
            "min_income": s.min_income,
            "max_income": s.max_income,
            "min_cgpa": s.min_cgpa,
            "eligible_categories": s.eligible_categories,
            "eligible_states": s.eligible_states,
        }
        results.append({"scholarship": sch_data, "score": score})

    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
    return sorted_results
