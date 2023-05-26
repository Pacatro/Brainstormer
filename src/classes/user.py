import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.getenv('PROJECT_PATH'))

from src.database.connection_db import conn
from src.functions.functions import generate_user_id, generate_hash

class User:
    def __init__(self, username: str, email: str, passwd: str) -> None:
        self.__user_id = generate_user_id() #--> IMPORTANTE: ENCONTRAR UNA FORMA DE GENERAR UN ID UNICO (UNO RANDOM NO SIRVE)
        self.__username = username
        self.__email = email
        self.__passwd = generate_hash(passwd)
        self.__cursor = conn.cursor()
    
    def get_user_id(self) -> int:
        return self.__user_id
    
    def get_username(self) -> str:
        return self.__username
        
    def is_in_db(self) -> bool:
        self.__cursor.execute(
            f'SELECT * FROM users WHERE user_id = {self.__user_id}'
        )
        
        return self.__cursor.fetchone() is not None
    
    def signup(self) -> None:
        self.__cursor.execute(
            f'INSERT INTO users (user_id, username, email, passwd) VALUES ({self.__user_id}, "{self.__username}", "{self.__email}", "{self.__passwd}")'
        )
        
        conn.commit()
