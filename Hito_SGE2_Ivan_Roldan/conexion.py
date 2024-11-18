import mysql.connector
from mysql.connector import Error

# Variable global para la conexión
conexion_global = None

def conectar():
    global conexion_global
    try:
        if conexion_global is None or not conexion_global.is_connected():
            conexion_global = mysql.connector.connect(
                host='localhost',
                user='root',
                password='campusfp',
                database='ENCUESTAS',
                use_pure=True
            )
            if conexion_global.is_connected():
                print("Conexión exitosa a la base de datos")
        return conexion_global
    except Error as e:
        print(f"Error al conectar: {e}")
        return None

def cerrar_conexion():
    global conexion_global
    if conexion_global and conexion_global.is_connected():
        conexion_global.close()
        print("Conexión cerrada")
