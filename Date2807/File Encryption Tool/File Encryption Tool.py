from cryptography.fernet import Fernet, InvalidToken
import os
from functools import wraps
import datetime

# ---------- Decorator ----------
def log_encryptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("encryption_log.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} - {func.__name__} was called.\n")
        return result
    return wrapper

# ---------- OOP ----------
class Cipher:
    def __init__(self, key_file='secret.key'):
        self.key_file = key_file
        self.key = None
        self.load_or_generate_key()

    def load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                self.key = f.read()
        else:
            self.key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(self.key)

        self.cipher = Fernet(self.key)

    @log_encryptions
    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            encrypted = self.cipher.encrypt(data)

            with open(file_path + ".enc", 'wb') as f:
                f.write(encrypted)

            print(f"✅ Encrypted and saved to: {file_path}.enc")
        except Exception as e:
            print(f"❌ Encryption failed: {e}")

    @log_encryptions
    def decrypt_file(self, encrypted_path):
        try:
            with open(encrypted_path, 'rb') as f:
                encrypted_data = f.read()
            decrypted = self.cipher.decrypt(encrypted_data)

            output_path = encrypted_path.replace(".enc", ".dec")
            with open(output_path, 'wb') as f:
                f.write(decrypted)

            print(f"✅ Decrypted and saved to: {output_path}")
        except InvalidToken:
            print("❌ Error: Wrong decryption key or corrupted file!")
        except Exception as e:
            print(f"❌ Decryption failed: {e}")

# ---------- CLI Usage ----------
def main():
    cipher = Cipher()

    print("\n🔐 File Encryption Tool")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Choose (1/2): ")

    file_path = input("Enter file path: ")

    if choice == '1':
        cipher.encrypt_file(file_path)
    elif choice == '2':
        cipher.decrypt_file(file_path)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
