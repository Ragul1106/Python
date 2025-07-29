from Crypto.Cipher import AES
import base64
import hashlib

BS = 16

def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def get_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt(raw, password):
    raw = pad(raw)
    key = get_key(password)
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(raw.encode())).decode()

def decrypt(enc, password):
    try:
        key = get_key(password)
        cipher = AES.new(key, AES.MODE_ECB)
        return unpad(cipher.decrypt(base64.b64decode(enc)).decode())
    except Exception:
        raise ValueError("Invalid encryption key.")
