# Experimental Characterization of Two-Qubit Entanglement on NISQ Hardware

This project presents a structured experimental study of two-qubit entanglement using Qiskit and IBM Quantum hardware. We benchmark ideal theoretical predictions against noisy simulations and real-device execution to analyze entanglement degradation in the NISQ regime.

---

## 🎯 Objectives

- Prepare the Bell state $|\Phi^+\rangle$
- Quantify entanglement using Von Neumann entropy
- Compare ideal, noisy-simulated, and hardware distributions
- Analyze statistical divergence due to noise
- Correlate entanglement degradation with backend parameters

---

## 🔬 Theoretical Background

The Bell state studied is:

$$
|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

To quantify entanglement, we compute the reduced density matrix:

$$
\rho_A = \mathrm{Tr}_B(\rho)
$$

The Von Neumann entropy is defined as:

$$
S(\rho_A) = - \mathrm{Tr}(\rho_A \log_2 \rho_A)
$$

For a maximally entangled Bell state:

$$
S = 1
$$

Deviations from unity indicate entanglement degradation due to noise.

---

## 🧪 Experimental Pipeline

1. **Ideal Statevector Simulation**
   - Density matrix construction
   - Partial trace
   - Entropy verification ($S = 1$)

2. **Measurement-Based Ideal Simulation**
   - 4096-shot Aer simulation

3. **Noise-Model Simulation**
   - Noise model derived from IBM backend
   - Noisy measurement statistics

4. **Statistical Divergence Analysis**
   - KL divergence (regularized)
   - Support mismatch interpretation

5. **Hardware Parameter Characterization**
   - $T_1$ relaxation time
   - $T_2$ dephasing time
   - Readout error
   - CNOT gate error

---

## 📊 Hardware Measurement Results (4096 Shots)

| State | Counts | Measured Probability | Ideal Probability | Deviation |
|:------|:-------|:--------------------|:------------------|:----------|
| $\lvert 00\rangle$ | 2101 | 51.2% | 50% | +1.2% |
| $\lvert 11\rangle$ | 1898 | 46.3% | 50% | −3.7% |
| $\lvert 01\rangle$ | 48   | 1.17% | 0%  | +1.17% |
| $\lvert 10\rangle$ | 49   | 1.19% | 0%  | +1.19% |

### Why do $|01\rangle$ and $|10\rangle$ appear?

In NISQ hardware, imperfections arise from:

- **Readout error**
- **Gate infidelity (CNOT errors)**
- **Decoherence processes ($T_1$, $T_2$)**

These effects introduce probability leakage into non-ideal states, reducing entanglement purity.

---

## ⚙ Backend Characterization

Hardware parameters influencing entanglement:

- $T_1$ — Energy relaxation time
- $T_2$ — Phase coherence time
- CNOT gate error rate
- Measurement (readout) error

This analysis connects device-level physics with quantum information metrics.

---

## 🛠 Setup

Install dependencies:

```bash
pip install qiskit qiskit-aer qiskit-ibm-runtime scipy matplotlib
```

## Save IBM Quantum token:

```python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token="YOUR_API_TOKEN"
)
```
## Run:
```script
Bell_State_Entanglement_Characterization.ipynb
```
