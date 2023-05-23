import random

def generate_user_id() -> int:
    return random.randint(0, 100000)

class User:
    def __init__(self, name: str, email: str, passwd: str) -> None:
        self.id = generate_user_id()
        self.name: name
        self.email: email
        self.passwd: passwd
        
    def get_id(self) -> int:
        return self.id