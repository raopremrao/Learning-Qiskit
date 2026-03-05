from qiskit import QuantumCircuit


def create_teleportation_circuit(theta):

    qc = QuantumCircuit(3,3)

    # Prepare quantum state to teleport
    qc.ry(theta,0)

    qc.barrier()

    # Create Bell pair
    qc.h(1)
    qc.cx(1,2)

    qc.barrier()

    # Alice operations
    qc.cx(0,1)
    qc.h(0)

    qc.barrier()

    # Measure Alice qubits
    qc.measure(0,0)
    qc.measure(1,1)

    # Conditional corrections
    with qc.if_test((qc.clbits[1],1)):
        qc.x(2)

    with qc.if_test((qc.clbits[0],1)):
        qc.z(2)

    qc.barrier()

    # Verification rotation
    qc.ry(-theta,2)

    qc.measure(2,2)

    return qc