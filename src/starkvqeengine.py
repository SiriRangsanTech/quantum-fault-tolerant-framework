import cirq
import numpy as np
from scipy.optimize import minimize
from stark_gate import StarkGate
from noise_model import build_noise_model
from hamiltonian_hubbard import build_hubbard_hamiltonian


def create_ansatz(qubits, theta):
    circuit = cirq.Circuit()
    for i, q in enumerate(qubits):
        circuit.append(cirq.ry(theta[i])(q))
    for i in range(len(qubits) - 1):
        circuit.append(cirq.CNOT(qubits[i], qubits[i + 1]))
    return circuit


def expectation_value(circuit, qubits, sampler):
    circuit.append(cirq.measure(*qubits, key="m"))
    result = sampler.run(circuit, repetitions=1000)
    hist = result.histogram(key="m")
    energy = sum(k * v for k, v in hist.items()) / 1000
    return energy


def objective(theta, qubits, sampler):
    circuit = create_ansatz(qubits, theta)
    return expectation_value(circuit, qubits, sampler)


def run_vqe():
    qubits = [cirq.GridQubit(0, i) for i in range(2)]
    sampler = cirq.Simulator(noise=build_noise_model())

    theta0 = np.random.uniform(0, 2 * np.pi, len(qubits))
    result = minimize(objective, theta0, args=(qubits, sampler), method="COBYLA")

    print("Optimal Energy:", result.fun)
    print("Optimal Parameters:", result.x)


if __name__ == "__main__":
    run_vqe()
