import mysql.connector
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv


def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="negocio"
    )

load_dotenv()

# Obtener la clave Fernet del archivo .env
FERNET_KEY = os.environ.get('FERNET_KEY')
cipher_suite = Fernet(FERNET_KEY)

