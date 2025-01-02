
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

IV = b'16-byte-initvect'

class MockQuantumSignal:
    def __init__(self, signal_id, quantum_state, noise_level, fidelity_metrics):
        self.signal_id = signal_id
        self.quantum_state = quantum_state
        self.noise_level = noise_level
        self.fidelity_metrics = fidelity_metrics

    def SerializeToString(self):
        return f"{self.signal_id},{self.quantum_state},{self.noise_level},{','.join(map(str, self.fidelity_metrics))}".encode('utf-8')

    @classmethod
    def ParseFromString(cls, data):
        decoded = data.decode('utf-8').split(',')
        return cls(decoded[0], decoded[1], float(decoded[2]), list(map(float, decoded[3:])))

def encrypt_protobuf_with_mock_corrected(obj, key):
    serialized_data = obj.SerializeToString()
    cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(serialized_data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(encrypted_data)

def decrypt_protobuf_with_mock_corrected(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data)
    cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    serialized_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
    return MockQuantumSignal.ParseFromString(serialized_data)
