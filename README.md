# Learning Qiskit: Quantum Research & Implementation

This repository documents my transition from theoretical quantum mechanics to hardware-level implementation using **Qiskit 1.0**. It features optimized workflows for preparing entangled states, analyzing NISQ-era hardware noise, and implementing research-grade transpilation strategies.

## Setup
1. Clone the repo: `git clone https://github.com/raopremrao/Learning-Qiskit.git`
2. Install requirements: `pip install -r requirements.txt`
3. Configure your IBM token: `QiskitRuntimeService.save_account(token='YOUR_TOKEN')`

## Tech Stack & Workflow
* **Language**: Python (Jupyter Notebooks)
* **OS**: Kali Linux
* **Quantum SDK**: Qiskit 1.0+ (Primitives V2)
* **Backend**: IBM Quantum Runtime Service

## Featured Projects

### 01. Bell State Preparation & Error Analysis
A study on preparing the $|\Phi^+\rangle$ state on physical superconducting processors.
* **Core Logic**: Implementing $H$ and $CNOT$ gates to create maximum entanglement.
* **Hardware**: Executed via `SamplerV2` on IBM Quantum backends.
* **Optimization**: Level 3 transpilation to mitigate gate errors and decoherence.

### 02. Quantum State Teleportation
This project implements and experimentally studies **quantum teleportation** using **Qiskit and IBM Quantum hardware**.

* **Core Logic**: Implementing the quantum teleportation protocol using Bell pairs and classical communication.

* **Hardware**: Executed on IBM Quantum backends.
* **Optimization**: Level 3 transpilation for error mitigation.

* **Results**: Demonstrates successful teleportation of an arbitrary qubit state with high fidelity.


### 03 Quantum Key Distribution (QKD)
This project implements **Quantum Key Distribution (QKD)** using Qiskit and IBM Quantum backends. The objective of this project is to demonstrate how two parties (Alice and Bob) can securely generate a shared secret key using quantum mechanics, and how an eavesdropper (Eve) can be detected if she tries to intercept the communication.

* **Core Logic**: Implementing the **BB84 Protocol** to establish a secure shared key using random basis encoding (Z and X bases).
* **Hardware**: Simulated using `AerSimulator` with custom noise models and executed on real IBM Quantum processors via `SamplerV2`.
* **Security Analysis**: Includes an eavesdropping simulation to demonstrate how measurement disturbance increases the Quantum Bit Error Rate (QBER) and lowers fidelity.
* **Optimization**: Utilizes `generate_preset_pass_manager` for hardware-specific transpilation and noise mitigation.

---
*Developed as part of my deep-dive into Quantum Computing.*