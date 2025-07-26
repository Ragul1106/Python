from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"
ENC_FILE = "passwords.enc"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def save_passwords(passwords):
    key = load_key()
    fernet = Fernet(key)
    data = "\n".join(passwords).encode()
    encrypted = fernet.encrypt(data)

    with open(ENC_FILE, "wb") as f:
        f.write(encrypted)
    print("Passwords saved securely to 'passwords.enc'.")

def read_passwords():
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(ENC_FILE, "rb") as f:
            encrypted_data = f.read()
        decrypted = fernet.decrypt(encrypted_data)
        return decrypted.decode().splitlines()
    except Exception:
        return []
