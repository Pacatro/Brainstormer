import random
import hashlib

def generate_user_id() -> int:
    return random.randint(0, 100000)

def generate_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()