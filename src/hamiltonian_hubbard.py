import numpy as np


def build_hubbard_hamiltonian(t=1.0, U=4.0, epsilon=0.0, V=0.0):
    return {
        "t": t,
        "U": U,
        "epsilon": epsilon,
        "V": V
    }
