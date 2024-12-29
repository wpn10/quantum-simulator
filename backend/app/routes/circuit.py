from fastapi import APIRouter, HTTPException
from app.services.circuit_service import create_circuit, simulate_circuit

router = APIRouter()

@router.post("/create")
async def create_circuit_endpoint(gates: list[dict]):
    """
    Create a quantum circuit based on the provided gate list.
    :param gates: List of gate dictionaries, e.g., [{'type': 'H', 'target': 0}]
    """
    try:
        circuit = create_circuit(gates)
        return {"circuit_diagram": circuit.draw(output="text")}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/simulate")
async def simulate_circuit_endpoint(gates: list[dict]):
    """
    Simulate a quantum circuit based on the provided gate list.
    :param gates: List of gate dictionaries, e.g., [{'type': 'H', 'target': 0}]
    """
    try:
        circuit = create_circuit(gates)
        result = simulate_circuit(circuit)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

