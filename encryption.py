
from cryptography.fernet import Fernet
import pickle

# Generate a key (hidden in the source code for now, ideally externalized)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(obj):
    serialized = pickle.dumps(obj)
    encrypted = cipher_suite.encrypt(serialized)
    return encrypted

def decrypt_message(encrypted_data):
    decrypted = cipher_suite.decrypt(encrypted_data)
    obj = pickle.loads(decrypted)
    return obj
