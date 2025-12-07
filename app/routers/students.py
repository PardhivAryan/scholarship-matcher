from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.database import get_db
from app.utils.jwt_handler import decode_token

router = APIRouter(prefix="/students", tags=["Students"])

def get_current_user(token: str, db: Session) -> User:
    try:
        payload = decode_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == payload.get("user_id")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/me")
def profile(token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "gender": user.gender,
        "income": user.income,
        "cgpa": user.cgpa,
        "category": user.category,
        "state": user.state,
    }

@router.put("/update")
def update_profile(
    token: str,
    age: int,
    gender: str,
    income: float,
    cgpa: float,
    category: str,
    state: str,
    db: Session = Depends(get_db),
):
    user = get_current_user(token, db)

    user.age = age
    user.gender = gender
    user.income = income
    user.cgpa = cgpa
    user.category = category
    user.state = state

    db.commit()
    return {"message": "Profile updated successfully"}
