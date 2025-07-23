import os

def simple_cipher(data: bytes, key: int = 42) -> bytes:
    return bytes([b ^ key for b in data])

def encrypt_file(filename: str):
    if not os.path.exists(filename):
        print("❌ File not found.")
        return

    with open(filename, "rb") as f:
        content = f.read()

    encrypted = simple_cipher(content)

    encrypted_filename = filename + "_encrypted.bin"
    with open(encrypted_filename, "wb") as f:
        f.write(encrypted)

    print(f"✅ Encrypted file saved as {encrypted_filename}")

def decrypt_file(filename: str):
    if not os.path.exists(filename):
        print("❌ File not found.")
        return

    with open(filename, "rb") as f:
        encrypted_content = f.read()

    decrypted = simple_cipher(encrypted_content)

    decrypted_filename = filename.replace("_encrypted.bin", "_decrypted.txt")
    with open(decrypted_filename, "wb") as f:
        f.write(decrypted)

    print(f"✅ Decrypted file saved as {decrypted_filename}")

def main():
    print("🔐 File Encryption & Decryption Tool")
    choice = input("1. Encrypt a file\n2. Decrypt a file\nChoose (1/2): ").strip()

    filename = input("Enter file name (with extension): ").strip()

    if choice == "1":
        encrypt_file(filename)
    elif choice == "2":
        decrypt_file(filename)
    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
