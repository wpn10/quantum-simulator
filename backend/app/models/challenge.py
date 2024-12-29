# backend/app/models/challenge.py
from sqlalchemy import Column, Integer, String, JSON
from app.models.database import Base

class QuantumChallenge(Base):
    __tablename__ = "quantum_challenges"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    solution = Column(JSON, nullable=True)
