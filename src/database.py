import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

conexion=mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    db=os.getenv('DATABASE')
)