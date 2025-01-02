
import unittest
import os
from src.framework import MockQuantumSignal, encrypt_protobuf_with_mock_corrected, decrypt_protobuf_with_mock_corrected

class TestFramework(unittest.TestCase):
    def setUp(self):
        self.test_key = os.urandom(32)  # AES-256 requires 32-byte key
        self.test_signal = MockQuantumSignal(
            signal_id="test123",
            quantum_state="state-vector",
            noise_level=0.01,
            fidelity_metrics=[0.95, 0.96, 0.97]
        )

    def test_serialization(self):
        serialized = self.test_signal.serialize()
        deserialized = MockQuantumSignal.deserialize(serialized)
        self.assertEqual(self.test_signal.signal_id, deserialized.signal_id)
        self.assertEqual(self.test_signal.quantum_state, deserialized.quantum_state)
        self.assertEqual(self.test_signal.noise_level, deserialized.noise_level)
        self.assertEqual(self.test_signal.fidelity_metrics, deserialized.fidelity_metrics)

    def test_encryption_decryption(self):
        encrypted_data = encrypt_protobuf_with_mock_corrected(self.test_signal, self.test_key)
        self.assertIsInstance(encrypted_data, bytes)

        decrypted_signal = decrypt_protobuf_with_mock_corrected(encrypted_data, self.test_key)
        self.assertEqual(self.test_signal.signal_id, decrypted_signal.signal_id)
        self.assertEqual(self.test_signal.quantum_state, decrypted_signal.quantum_state)
        self.assertEqual(self.test_signal.noise_level, decrypted_signal.noise_level)
        self.assertEqual(self.test_signal.fidelity_metrics, decrypted_signal.fidelity_metrics)

    def test_invalid_key(self):
        encrypted_data = encrypt_protobuf_with_mock_corrected(self.test_signal, self.test_key)
        invalid_key = os.urandom(32)
        with self.assertRaises(Exception):  # Expecting a decryption failure
            decrypt_protobuf_with_mock_corrected(encrypted_data, invalid_key)

if __name__ == "__main__":
    unittest.main()
