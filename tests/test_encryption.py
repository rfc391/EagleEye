import os
from core.framework import QuantumSignal, encrypt_signal

def test_encryption():
    signal = QuantumSignal("sigtest", "testState", 0.01, [0.99])
    key = os.urandom(32)
    encrypted = encrypt_signal(signal, key)
    assert encrypted is not None