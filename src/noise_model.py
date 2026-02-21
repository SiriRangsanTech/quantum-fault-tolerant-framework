import cirq


def build_noise_model(T=0.1):
    gamma = T**5

    noise_ops = [
        cirq.amplitude_damp(gamma),
        cirq.phase_damp(gamma)
    ]

    return cirq.NoiseModel.from_noise_ops(noise_ops)
