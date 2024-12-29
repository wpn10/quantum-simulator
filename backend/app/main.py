from fastapi import FastAPI
from app.routes.circuit import router as circuit_router
from app.models.database import SessionLocal
from app.models.challenge import QuantumChallenge

app = FastAPI(title="Quantum Circuit Simulator")

app.include_router(circuit_router, prefix="/circuit", tags=["Quantum Circuits"])

@app.on_event("startup")
def populate_database():
    session = SessionLocal()
    try:
        challenges = [
            {
                "name": "Quantum Fourier Transform",
                "description": "Implement a 3-qubit Quantum Fourier Transform.",
                "solution": {"steps": ["H 0", "CR 1 0 π/2", "H 1", "SWAP 0 2"]},
            },
            {
                "name": "Bell State",
                "description": "Create a Bell State using 2 qubits.",
                "solution": {"steps": ["H 0", "CX 0 1"]},
            },
            {
                "name": "GHZ State",
                "description": "Create a GHZ state with 3 qubits.",
                "solution": {"steps": ["H 0", "CX 0 1", "CX 0 2"]},
            },
        ]
        for challenge in challenges:
            existing_challenge = session.query(QuantumChallenge).filter_by(name=challenge["name"]).first()
            if not existing_challenge:
                session.add(QuantumChallenge(**challenge))
        session.commit()
        print("Database populated with initialchallenges!")
    except Exception as e:
        print(f"Error populating database: {e}")
        session.rollback()
    finally:
        session.close()

@app.get("/")
def root():
    return {"message": "Welcome to the Quantum Computing Simulator API"}