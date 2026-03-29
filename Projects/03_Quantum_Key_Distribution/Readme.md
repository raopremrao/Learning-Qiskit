# Quantum Key Distribution (QKD) using Qiskit

## Project Overview
This project implements **Quantum Key Distribution (QKD)** using Qiskit and IBM Quantum backends. The objective of this project is to demonstrate how two parties (Alice and Bob) can securely generate a shared secret key using quantum mechanics, and how an eavesdropper (Eve) can be detected if she tries to intercept the communication.

This project includes:
- QKD without eavesdropping
- QKD with eavesdropping
- Noisy simulator execution
- Real quantum computer execution
- Fidelity comparison
- Eavesdropper detection

The protocol implemented is based on the **BB84 Quantum Key Distribution Protocol**.

---

## Table of Contents
1. Introduction  
2. Quantum Key Distribution Theory  
3. BB84 Protocol Steps  
4. Project Workflow  
5. Installation  
6. Libraries Used  
7. QKD Without Eavesdropper  
8. QKD With Eavesdropper  
9. Noise Simulation  
10. Running on Real Quantum Hardware  
11. Fidelity Calculation  
12. Results  
13. Key Concepts Used  
14. Future Improvements  
15. Applications  
16. Conclusion  

---

## Introduction
Classical cryptography relies on mathematical hardness for security. However, quantum computers can break many classical encryption methods. Quantum Key Distribution (QKD) provides **information-theoretic security** using the principles of quantum mechanics.

QKD is based on the following quantum principles:
- Superposition
- Measurement collapse
- No-cloning theorem
- Measurement disturbance
- Random basis encoding

Because measuring a quantum state disturbs it, an eavesdropper can always be detected.

---

## Quantum Key Distribution Theory
Quantum Key Distribution allows two parties:
- Alice (Sender)
- Bob (Receiver)

to share a secret key securely. If an eavesdropper (Eve) tries to measure the qubits, the quantum states change, introducing errors that Alice and Bob can detect.

Two bases are used:
- Z basis (|0⟩, |1⟩)
- X basis (|+⟩, |−⟩)

Encoding table:

| Bit | Basis | State | Gate |
|-----|------|------|------|
| 0 | Z | |0⟩ | I |
| 1 | Z | |1⟩ | X |
| 0 | X | |+⟩ | H |
| 1 | X | |−⟩ | X + H |

---

## BB84 Protocol Steps
1. Alice generates random bits
2. Alice generates random bases
3. Alice encodes qubits using bits and bases
4. Alice sends qubits to Bob
5. Bob randomly chooses measurement bases
6. Bob measures qubits
7. Alice and Bob publicly compare bases
8. They keep only bits where bases matched
9. They compare a few bits to check for eavesdropping
10. Remaining bits become the secret key

If Eve intercepts the qubits, she introduces errors which reduce fidelity.

---

## Project Workflow
The workflow implemented in this project:

Alice bits → Encode qubits → Send qubits →
Eve intercepts (optional) →
Bob measures → Compare bases →
Keep matched bits → Compute fidelity → Detect Eve


---

## Installation
Install required libraries:

```bash
pip install qiskit
pip install qiskit-aer
pip install qiskit-ibm-runtime
pip install numpy
```

## Login to IBM Quantum:

```python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(channel="ibm_quantum", token="YOUR_API_TOKEN")
```

## Libraries Used:

1. Qiskit
2. Qiskit Aer
3. Qiskit IBM Runtime
4. NumPy

*Imports used in project:*
```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.primitives import BackendSamplerV2

from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel

from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
```

---

## QKD Without Eavesdropper

Steps:

1. Alice generates random bits and bases
2. Alice encodes qubits
3. Bob chooses random bases
4. Bob measures qubits
5. Alice and Bob compare bases
6. Keep only matched bits
7. Calculate fidelity

If no eavesdropper exists, fidelity should be close to 1.

---

## QKD With Eavesdropper

In this case:

1. Eve intercepts qubits
2. Eve measures qubits in random bases
3. Eve resends qubits to Bob
4. Measurement disturbs qubits
5. Bob measures disturbed qubits
6. Alice and Bob compare bits
7. Fidelity decreases
8. Eve is detected

This demonstrates measurement disturbance and no-cloning theorem.

---
## Noise Simulation

Real quantum computers have noise such as:

* Gate errors
* Measurement errors
* Decoherence
* Readout errors

To simulate real hardware noise:
```python
NoiseModel.from_backend(backend)
AerSimulator(noise_model=noise_model)
```
This makes the simulation realistic.

---

## Running on Real Quantum Hardware

Steps:

1. Connect to IBM Quantum
2. Select least busy backend
3. Transpile circuit
4. Run sampler
5. Get counts
6. Convert counts to bit string
7. Compare Alice and Bob bits
8. Calculate fidelity 

---

## Fidelity Calculation

After basis comparison:
```
Fidelity = Matching Bits / Total Matched Bits
Loss = 1 - Fidelity
```

If fidelity is low → Eavesdropper detected
If fidelity is high → Secure communication

---

## Example Results

| Scenario | Fidelity | Loss |
|-----|------|------|
| No Eavesdropper | ~0.98 | ~0.02 |
| With Eavesdropper | ~0.70 | ~0.30 |

This clearly shows that eavesdropping introduces errors.

--- 
## Key Concepts Used

This project uses many quantum computing concepts:

* Qubits
* Quantum gates (H, X)
* Measurement
* Superposition
* Quantum noise
* Transpilation
* Noise model
* Fidelity
* BB84 Protocol
* Quantum cryptography
* IBM Quantum Runtime
* Aer Simulator

---

## Future Improvements

Possible extensions:

* Error correction
* Privacy amplification
* Multi-shot statistics
* Fidelity vs noise graph
* Different eavesdropping strategies
* Entanglement-based QKD (E91)
* Secure key rate calculation
* Bloch sphere visualization
* Web interface for simulation

---

## Applications of QKD

Quantum Key Distribution is used in:

* Military communication
* Banking security
* Government communication
* Satellite quantum communication
* Quantum internet
* Secure voting systems

China already has quantum communication satellites using QKD.

---

## Conclusion

This project demonstrates that:

* Quantum mechanics can be used for secure communication
* Eavesdropping can always be detected
* Noise affects fidelity but secure communication is still possible
* QKD is one of the most important real-world applications of quantum computing

This project combines:

* Quantum circuits
* Noise simulation
* Real quantum hardware
* Cryptography
* Fidelity analysis

--- 

## Author

**Project**: Quantum Key Distribution using Qiskit

**Tools Used**: Python, Qiskit, IBM Quantum, Aer Simulator

**Field**: Quantum Computing / Quantum Cryptography

**Author**: T Prem


---
