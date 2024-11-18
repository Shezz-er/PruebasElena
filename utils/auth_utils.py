
from database import obtener_conexion, cipher_suite
from cryptography.fernet import InvalidToken

def autenticar_usuario(rut, password):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT password FROM usuarios WHERE rut = %s", (rut,))
    result = cursor.fetchone()
    conexion.close()
    if result:
        stored_password = result['password']
        try:
            decrypted_password = cipher_suite.decrypt(stored_password.encode()).decode()
            return decrypted_password == password
        except InvalidToken:
            return False
    return False
