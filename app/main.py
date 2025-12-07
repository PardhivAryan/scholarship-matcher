from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, students, scholarships

# Create tables on startup (simple dev approach)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scholarship Matching Platform")

app.include_router(auth.router)
app.include_router(students.router)
app.include_router(scholarships.router)

@app.get("/")
def root():
    return {"message": "API is running!"}
