
import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

class QuantumSignal:
    def __init__(self, signal_id, quantum_state, noise_level, fidelity_metrics):
        self.signal_id = signal_id
        self.quantum_state = quantum_state
        self.noise_level = noise_level
        self.fidelity_metrics = fidelity_metrics

    def serialize(self):
        """Custom serialization into a secure format."""
        serialized = f"{self.signal_id}|{self.quantum_state}|{self.noise_level}|{','.join(map(str, self.fidelity_metrics))}"
        return serialized.encode()

    @staticmethod
    def deserialize(data):
        """Custom deserialization from the secure format."""
        decoded = data.decode()
        parts = decoded.split("|")
        return QuantumSignal(
            signal_id=parts[0],
            quantum_state=parts[1],
            noise_level=float(parts[2]),
            fidelity_metrics=list(map(float, parts[3].split(",")))
        )

def encrypt_signal(signal, key):
    """Encrypt a serialized signal using AES-256."""
    backend = default_backend()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    encryptor = cipher.encryptor()

    serialized_data = signal.serialize()
    padded_data = padder.update(serialized_data) + padder.finalize()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(iv + encrypted)

def decrypt_signal(encrypted_data, key):
    """Decrypt an encrypted signal back to its original form."""
    backend = default_backend()
    decoded_data = base64.b64decode(encrypted_data)
    iv = decoded_data[:16]
    encrypted = decoded_data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

    decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

    return QuantumSignal.deserialize(decrypted)
