
from core.framework import QuantumSignal, encrypt_signal
import os

def main():
    # Sample quantum signal data
    signal = QuantumSignal("sig001", "stateABC", 0.02, [0.95, 0.92, 0.91])
    
    # Generate a random encryption key (AES-256)
    encryption_key = os.urandom(32)
    
    print("Original Signal:")
    print(f"ID: {signal.signal_id}, State: {signal.quantum_state}, Noise Level: {signal.noise_level}, Metrics: {signal.fidelity_metrics}")
    
    # Encrypt the signal
    try:
        encrypted_data = encrypt_signal(signal, encryption_key)
        print("Signal encrypted successfully.")
    except Exception as e:
        print(f"Encryption failed: {e}")

if __name__ == "__main__":
    main()
