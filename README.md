# ⚛️ Learning Qiskit: Quantum Research & Implementation

This repository documents my transition from theoretical quantum mechanics to hardware-level implementation using **Qiskit 1.0**. It features optimized workflows for preparing entangled states, analyzing NISQ-era hardware noise, and implementing research-grade transpilation strategies.

## 📌 Setup
1. Clone the repo: `git clone https://github.com/raopremrao/Learning-Qiskit.git`
2. Install requirements: `pip install -r requirements.txt`
3. Configure your IBM token: `QiskitRuntimeService.save_account(token='YOUR_TOKEN')`

## 🛠️ Tech Stack & Workflow
* **Language**: Python (Jupyter Notebooks)
* **OS**: Kali Linux
* **Quantum SDK**: Qiskit 1.0+ (Primitives V2)
* **Backend**: IBM Quantum Runtime Service

## 🚀 Featured Projects

### 01. Bell State Preparation & Error Analysis
A study on preparing the $|\Phi^+\rangle$ state on physical superconducting processors.
* **Core Logic**: Implementing $H$ and $CNOT$ gates to create maximum entanglement.
* **Hardware**: Executed via `SamplerV2` on IBM Quantum backends.
* **Optimization**: Level 3 transpilation to mitigate gate errors and decoherence.

---
*Developed as part of my deep-dive into Quantum Computing.*