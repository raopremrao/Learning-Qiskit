import numpy as np


def compute_fidelity(counts, shots):

    success = 0

    for bitstring, count in counts.items():

        if bitstring[0] == '0':
            success += count

    fidelity = success / shots

    return fidelity


def fidelity_table(angle_list, fidelity_list):

    for angle, fidelity in zip(angle_list, fidelity_list):

        print(f"Theta: {angle:.3f}  Fidelity: {fidelity:.3f}")