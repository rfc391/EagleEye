
# Usage Guide

## Core Classes and Functions
- `MockQuantumSignal`: Simulates a Protocol Buffer schema for quantum signals.
- `encrypt_protobuf_with_mock_corrected`: Encrypts a serialized quantum signal object.
- `decrypt_protobuf_with_mock_corrected`: Decrypts and deserializes the encrypted data.

## Example Workflow
```python
# Create a test signal
test_signal = MockQuantumSignal(
    signal_id="sig123",
    quantum_state="state-vector",
    noise_level=0.02,
    fidelity_metrics=[0.99, 0.97, 0.98]
)

# Encrypt the signal
encrypted_data = encrypt_protobuf_with_mock_corrected(test_signal, test_key)

# Decrypt the signal
decrypted_signal = decrypt_protobuf_with_mock_corrected(encrypted_data, test_key)
```
