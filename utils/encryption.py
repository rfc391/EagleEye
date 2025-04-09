
# encryption.py
def encrypt_message(message):
    return f"encrypted({message})"

def decrypt_message(message):
    return message.replace("encrypted(", "").rstrip(")")
