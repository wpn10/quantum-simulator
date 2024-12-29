from fastapi import FastAPI
from app.routes.circuit import router as circuit_router

app = FastAPI(title="Quantum Circuit Simulator")

app.include_router(circuit_router, prefix="/circuit", tags=["Quantum Circuits"])

@app.get("/")
def root():
    return {"message": "Welcome to the Quantum Computing Simulator API"}