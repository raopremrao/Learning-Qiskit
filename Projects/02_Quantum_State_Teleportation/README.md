# Quantum Teleportation Fidelity Study

## Overview

This project implements and experimentally studies **quantum teleportation** using **Qiskit and IBM Quantum hardware**.

The objective is to teleport arbitrary quantum states and evaluate teleportation fidelity on both:

* Ideal simulator
* Real noisy quantum hardware

## Teleportation Protocol

Quantum teleportation transfers an unknown quantum state

|ψ⟩ = α|0⟩ + β|1⟩

from Alice to Bob using:

* Shared Bell pair
* Classical communication
* Conditional correction operations.

## Experiments

The experiment teleports states parameterized by:

ψ(θ) = Ry(θ)|0⟩

Angles tested:

0, π/6, π/4, π/3, π/2

For each state:

1. Teleportation circuit is executed
2. Simulator fidelity is measured
3. Hardware fidelity is measured
4. Results are compared.

## Teleportation Fidelity

After teleportation we apply the inverse rotation:

Ry(-θ)

If teleportation succeeds, the final state should be:

|0⟩

Fidelity is computed as:

F = P(0)

## Tools

* Qiskit
* IBM Quantum Runtime
* SamplerV2
* AerSimulator
* Matplotlib

## Results

Hardware fidelity is lower due to:

* CNOT gate errors
* Decoherence
* Measurement noise

## Repository Structure

teleportation_circuit.py
Defines teleportation circuit.

fidelity_analysis.py
Computes teleportation fidelity.

teleportation_experiment.ipynb
Runs experiments and generates plots.

results/
Stores measurement results.

figures/
Stores plots.
