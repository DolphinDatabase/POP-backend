import hashlib


def hash_password(password: str) -> str:
    password_bytes = bytes(password)
    hashed_password = hashlib.sha256(password_bytes)
    return hashed_password.digest()
