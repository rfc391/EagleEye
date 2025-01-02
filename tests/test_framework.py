
import unittest
from src import MockQuantumSignal, encrypt_protobuf_with_mock_corrected, decrypt_protobuf_with_mock_corrected

class TestQuantumSignalFramework(unittest.TestCase):
    def setUp(self):
        self.test_key = b'16-byte-long-key'
        self.test_signal = MockQuantumSignal(
            signal_id="sig123",
            quantum_state="state-vector",
            noise_level=0.02,
            fidelity_metrics=[0.99, 0.97, 0.98]
        )

    def test_encryption_decryption(self):
        encrypted_data = encrypt_protobuf_with_mock_corrected(self.test_signal, self.test_key)
        decrypted_signal = decrypt_protobuf_with_mock_corrected(encrypted_data, self.test_key)
        self.assertEqual(self.test_signal.signal_id, decrypted_signal.signal_id)
        self.assertEqual(self.test_signal.quantum_state, decrypted_signal.quantum_state)
        self.assertAlmostEqual(self.test_signal.noise_level, decrypted_signal.noise_level)
        self.assertListEqual(self.test_signal.fidelity_metrics, decrypted_signal.fidelity_metrics)

if __name__ == "__main__":
    unittest.main()
