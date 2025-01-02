
import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

class MockQuantumSignal:
    def __init__(self, signal_id, quantum_state, noise_level, fidelity_metrics):
        self.signal_id = signal_id
        self.quantum_state = quantum_state
        self.noise_level = noise_level
        self.fidelity_metrics = fidelity_metrics

    def serialize(self):
        return f"{self.signal_id}|{self.quantum_state}|{self.noise_level}|{','.join(map(str, self.fidelity_metrics))}".encode()

    @staticmethod
    def deserialize(data):
        components = data.decode().split("|")
        fidelity_metrics = list(map(float, components[3].split(",")))
        return MockQuantumSignal(components[0], components[1], float(components[2]), fidelity_metrics)

def encrypt_protobuf_with_mock_corrected(obj, key):
    backend = default_backend()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    iv = os.urandom(16)  # Dynamically generated IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    serialized_data = obj.serialize()
    padded_data = padder.update(serialized_data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_data)

def decrypt_protobuf_with_mock_corrected(data, key):
    backend = default_backend()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decoded_data = base64.b64decode(data)
    iv = decoded_data[:16]  # Extract IV
    encrypted_data = decoded_data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return MockQuantumSignal.deserialize(plaintext)
