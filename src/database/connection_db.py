import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

conn = pymysql.connect(
    host=os.getenv('DB_HOST'), port=int(os.getenv('DB_PORT')), user=os.getenv('DB_USER'), 
    passwd=os.getenv('DB_PASSWD'), db=os.getenv('DB_NAME')
)