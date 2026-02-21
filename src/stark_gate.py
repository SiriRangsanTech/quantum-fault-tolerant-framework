import cirq
import numpy as np


class StarkGate(cirq.Gate):
    def __init__(self, alpha1=0.1, alpha2=0.01, voltage=1.0, duration=1.0):
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.voltage = voltage
        self.duration = duration

    def _unitary_(self):
        E = self.voltage
        phi = (self.alpha1 * E + self.alpha2 * E**2) * self.duration
        return cirq.unitary(cirq.rz(phi))

    def num_qubits(self):
        return 1

    def __str__(self):
        return f"StarkGate(V={self.voltage})"
