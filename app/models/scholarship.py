from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Scholarship(Base):
    __tablename__ = "scholarships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    description = Column(String, nullable=True)

    min_income = Column(Float, nullable=True)
    max_income = Column(Float, nullable=True)
    min_cgpa = Column(Float, nullable=True)

    # Stored as comma-separated strings (e.g., "SC,OBC,GENERAL")
    eligible_categories = Column(String, nullable=True)
    eligible_states = Column(String, nullable=True)
