# backend/app/routes/challenge.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.challenge import QuantumChallenge

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_challenges(db: Session = Depends(get_db)):
    challenges = db.query(QuantumChallenge).all()
    return [
        {"id": c.id, "name": c.name, "description": c.description} for c in challenges
    ]
