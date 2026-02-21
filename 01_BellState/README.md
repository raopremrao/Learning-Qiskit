# Quantum Entanglement: Bell State Preparation on IBM Hardware

This project implements the preparation and measurement of the $|\Phi^+\rangle$ Bell State using **Qiskit 1.0** and the **Qiskit Runtime Service**. It transitions from theoretical simulation to physical execution on IBM's superconducting quantum processors, providing a deep dive into error analysis and NISQ-era hardware constraints.

## 🚀 Key Features
* **Modular Design**: Circuit factory pattern for generating all four Bell Basis states.
* **Hardware Integration**: Automated backend selection via `QiskitRuntimeService`.
* **Advanced Transpilation**: Optimization Level 3 for high-fidelity gate mapping.
* **V2 Primitives**: Implementation of the latest `SamplerV2` for hardware execution.

---

## 🔬 Physics & Theory
A Bell state is a maximally entangled quantum state of two qubits. We focus on:
$$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

### Circuit Implementation
1.  **Hadamard Gate ($H$)**: Places the first qubit into a superposition.
2.  **CNOT Gate**: Entangles the two qubits, mapping the state of the first onto the second.



---

## 📊 Experimental Results & Error Analysis

Data collected from physical hardware (**4096 shots**) shows the impact of noise on quantum systems:

| State | Counts | Probability | Ideal |
| :--- | :--- | :--- | :--- |
| $\|00\rangle$ | 2028 | 49.5% | 50% |
| $\|11\rangle$ | 1891 | 46.1% | 50% |
| $\|01\rangle$ | 91   | 2.2%  | 0% |
| $\|10\rangle$ | 32   | 0.7%  | 0% |

### Why do $|01\rangle$ and $|10\rangle$ exist?
In the **NISQ (Noisy Intermediate-Scale Quantum)** era, physical hardware is subject to environmental and operational noise:
* **Readout Error**: Misidentification of qubit states during the measurement process.
* **Gate Infidelity**: Fluctuations in the microwave pulses used for the CNOT operation.
* **Decoherence ($T_1$/$T_2$)**: Spontaneous energy relaxation and phase loss due to coupling with the external environment.
---

## 🛠️ Setup & Usage
1.  **Install Dependencies**:
    ```bash
    pip install qiskit qiskit-ibm-runtime matplotlib
    ```
2.  **Configure API Key**:
    Save your IBM Quantum token locally:
    ```python
    from qiskit_ibm_runtime import QiskitRuntimeService
    QiskitRuntimeService.save_account(channel="ibm_quantum_platform", token="YOUR_TOKEN")
    ```
3.  **Run the Notebook**: Open `BellState.ipynb` and execute the cells.

---

## 🛠️ Mitigation Strategy
This project utilizes **Resilience Level 1** to enable **TREX (Twirled Readout Error eXtinction)**, which mathematically mitigates measurement bias.