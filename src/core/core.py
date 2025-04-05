import os
from core.framework import QuantumSignal, encrypt_signal

def run_signal_encryption():
    signal = QuantumSignal("sig001", "stateABC", 0.02, [0.95, 0.92, 0.91])
    encryption_key = os.urandom(32)

    print("Original Signal:")
    print(f"ID: {signal.signal_id}, State: {signal.quantum_state}, Noise: {signal.noise_level}, Metrics: {signal.fidelity_metrics}")

    try:
        encrypted_data = encrypt_signal(signal, encryption_key)
        print("Signal encrypted successfully.")
    except Exception as e:
        print(f"Encryption failed: {e}")