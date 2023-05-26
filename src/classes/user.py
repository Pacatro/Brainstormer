import sys
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.getenv('PROJECT_PATH'))

from src.database.connection_db import conn
from src.functions.functions import generate_hash

class User:
    def __init__(self, email: str, passwd: str, username: str = "") -> None:
        self.__user_id: int
        self.__email = email
        self.__passwd = generate_hash(passwd)
        self.__username = username
        self.__cursor = conn.cursor()
    
    def get_user_id(self) -> int:
        self.__cursor.execute(
            f'SELECT user_id FROM users WHERE email = "{self.__email}"'
        )
        
        self.__user_id = self.__cursor.fetchone()[0]
        
        return self.__user_id
    
    def get_username(self) -> str:
        if self.__username != "":
            return self.__username
        
        self.__cursor.execute(
            f'SELECT username FROM users WHERE email = "{self.__email}" AND passwd = "{self.__passwd}"'
        )
        
        self.__username = self.__cursor.fetchone()[0]
        
        return self.__username
        
    def is_in_db(self) -> bool:
        self.__cursor.execute(
            f'SELECT * FROM users WHERE email = "{self.__email}" AND passwd = "{self.__passwd}"'
        )
        
        return self.__cursor.fetchone() is not None
    
    def signup(self) -> None:
        self.__cursor.execute(
            f'INSERT INTO users (username, email, passwd) VALUES ("{self.__username}", "{self.__email}", "{self.__passwd}")'
        )
        
        conn.commit()
