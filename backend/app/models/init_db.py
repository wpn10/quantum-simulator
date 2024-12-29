# backend/app/models/init_db.py
from app.models.database import Base, engine
from app.models.challenge import QuantumChallenge

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized!")
