# ⚛️ Learning Qiskit: Quantum Research & Implementation

This repository documents my transition from theoretical quantum mechanics to hardware-level implementation using **Qiskit 1.0**. It features optimized workflows for preparing entangled states, analyzing NISQ-era hardware noise, and implementing research-grade transpilation strategies.

## 🚀 Featured Projects

### 01. Bell State Preparation & Error Analysis
A study on preparing the $|\Phi^+\rangle$ state on physical superconducting processors.
* **Core Logic**: Implementing $H$ and $CNOT$ gates to create maximum entanglement.
* **Hardware**: Executed via `SamplerV2` on IBM Quantum backends.
* **Optimization**: Level 3 transpilation to mitigate gate errors and decoherence.

---

## 🔬 Experimental Results & Hardware Analysis

Data collected from physical hardware (**4096 shots**) demonstrates the real-world performance of quantum bits compared to ideal simulators.

| State | Counts | Probability | Ideal (Simulated) |
| :--- | :--- | :--- | :--- |
| $\|00\rangle$ | 2085 | 50.9% | 50% |
| $\|11\rangle$ | 1948 | 47.6% | 50% |
| $\|01\rangle$ | 31   | 0.7%  | 0% |
| $\|10\rangle$ | 32   | 0.8%  | 0% |

> **Calculated Fidelity**: $F \approx 98.4\%$

### The "NISQ" Fingerprint: Why do $|01\rangle$ and $|10\rangle$ appear?
In physical hardware, unwanted states occur due to:
1. **Readout Error**: Misidentification of qubit states during measurement signal integration.
2. **Gate Infidelity**: Microwave pulse fluctuations during the CNOT operation.
3. **Decoherence ($T_1$/$T_2$)**: Spontaneous relaxation and phase loss due to environmental coupling.

---

## 🛠️ Tech Stack & Workflow
* **Language**: Python (Jupyter Notebooks)
* **OS**: Kali Linux
* **Quantum SDK**: Qiskit 1.0+ (Primitives V2)
* **Backend**: IBM Quantum Runtime Service


## 📌 Setup
1. Clone the repo: `git clone https://github.com/raopremrao/Learning-Qiskit.git`
2. Install requirements: `pip install -r requirements.txt`
3. Configure your IBM token: `QiskitRuntimeService.save_account(token='YOUR_TOKEN')`

---
*Developed as part of my deep-dive into Quantum Computing.*