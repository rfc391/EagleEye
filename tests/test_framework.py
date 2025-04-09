
import unittest
import os
from EagleEye.core.framework import QuantumSignal, encrypt_signal, decrypt_signal

class TestQuantumSignal(unittest.TestCase):
    def setUp(self):
        self.test_key = os.urandom(32)
        self.signal = QuantumSignal(
            signal_id="signal123",
            quantum_state="state-vector",
            noise_level=0.02,
            fidelity_metrics=[0.98, 0.97, 0.96]
        )

    def test_serialization_deserialization(self):
        serialized = self.signal.serialize()
        deserialized = QuantumSignal.deserialize(serialized)
        self.assertEqual(self.signal.signal_id, deserialized.signal_id)
        self.assertEqual(self.signal.quantum_state, deserialized.quantum_state)
        self.assertEqual(self.signal.noise_level, deserialized.noise_level)
        self.assertEqual(self.signal.fidelity_metrics, deserialized.fidelity_metrics)

    def test_encryption_decryption(self):
        encrypted = encrypt_signal(self.signal, self.test_key)
        self.assertIsInstance(encrypted, bytes)
        decrypted = decrypt_signal(encrypted, self.test_key)
        self.assertEqual(self.signal.signal_id, decrypted.signal_id)

    def test_invalid_key(self):
        encrypted = encrypt_signal(self.signal, self.test_key)
        invalid_key = os.urandom(32)
        with self.assertRaises(Exception):
            decrypt_signal(encrypted, invalid_key)

if __name__ == "__main__":
    unittest.main()
