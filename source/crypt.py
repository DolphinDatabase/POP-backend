import hashlib
from cryptography.fernet import Fernet


def hash_password(password: str) -> str:
    password_bytes = bytes(password, encoding='utf-8')
    hashed_password = hashlib.sha256(password_bytes)
    return hashed_password.hexdigest()


def encrypt_data(data: str, key: str) -> str:
    cipher = Fernet(key)
    data_bytes = bytes(data, encoding='utf-8')
    encoded_data = cipher.encrypt(data_bytes)
    return encoded_data.decode(encoding='utf-8')


def decrypt_data(data: str, key: str) -> str:
    cipher = Fernet(key)
    data_bytes = bytes(data, encoding='utf-8')
    decoded_data = cipher.decrypt(data_bytes)
    return decoded_data.decode(encoding='utf-8')


def generate_random_key() -> str:
    return Fernet.generate_key().decode(encoding='utf-8')
