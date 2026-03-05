import numpy as np

def compute_error_bar(fidelity, shots):

    sigma = np.sqrt((fidelity * (1 - fidelity)) / shots)

    return sigma