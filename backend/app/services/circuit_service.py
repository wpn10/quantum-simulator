from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.primitives import BackendEstimator

def create_circuit(gates: list[dict]):
    """
    Create a QuantumCircuit based on the provided gate list.
    :param gates: List of gate dictionaries, e.g., [{'type': 'H', 'target': 0}]
    """
    num_qubits = max(gate['target'] for gate in gates) + 1
    circuit = QuantumCircuit(num_qubits)
    for gate in gates:
        if gate['type'] == 'H':
            circuit.h(gate['target'])
        elif gate['type'] == 'X':
            circuit.x(gate['target'])
    return circuit

def simulate_circuit(circuit: QuantumCircuit, backend: str = "qasm_simulator") -> dict:
    backend = Aer.get_backend(backend)
    job = backend.run(circuit, shots=1024)
    result = job.result()
    counts = result.get_counts(circuit)
    return counts
