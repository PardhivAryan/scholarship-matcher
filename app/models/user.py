from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    income = Column(Float, nullable=True)
    cgpa = Column(Float, nullable=True)
    category = Column(String, nullable=True)  # e.g., SC/ST/OBC/General
    state = Column(String, nullable=True)
