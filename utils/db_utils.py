import mysql.connector


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooserIconView
import mysql.connector
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import mysql.connector
import tempfile
import os
import base64
from io import BytesIO
import uuid
from PIL import Image as PILImage
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from widgets.producto_item import *
from widgets import *
from database import *



def obtener_opciones(query):
    conexion = mysql.connector.connect(database= "negocio", user="root")
    cursor = conexion.cursor()
    try:
        cursor.execute(query)
        resultados = cursor.fetchall()
        opciones = [fila[0] for fila in resultados]
        print(opciones)  # Imprimir para verificar
        return opciones
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return []  # Retornar lista vacía en caso de error
    finally:
        cursor.close()
        conexion.close()


def insertar_producto(nombre_producto, precio_venta, 
    desc_producto, image_blob, costo, stock, fecha_vencimiento, cantidad_minima, 
    id_medida, id_proveedor, ubicacion, id_categoria, barcode):

    query = """INSERT INTO productos (nombre_producto, precio_venta, 
    desc_producto, image_blob, costo, stock, fecha_vencimiento, cantidad_minima, 
    id_medida, id_proveedor, ubicacion, id_categoria, barcode) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    conexion = mysql.connector.connect(database= "negocio", user="root")
    cursor = conexion.cursor()
    cursor.execute(query, (nombre_producto, precio_venta, desc_producto, image_blob, costo, stock, fecha_vencimiento, cantidad_minima, id_medida, id_proveedor, ubicacion, id_categoria, barcode))
    conexion.commit()
    # self.ids.resultado_label.text = 'Producto agregado exitosamente'



def agregar_producto(self):
    conexion = mysql.connector.connect(database= "negocio", user="root")
    cursor = conexion.cursor()

    nombre_producto = self.ids.nombre_producto_input.text
    desc_producto = self.ids.desc_producto_input.text
    costo = self.ids.costo_input.text
    precio_venta = self.ids.precio_input.text
    stock = self.ids.stock_input.text
    fecha_vencimiento = self.ids.fecha_vencimiento_input.text  # Asegúrate de que esto sea correcto
    cantidad_minima = self.ids.cantidad_minima_input.text
    id_medida = self.ids.spinner_medida.text  # Valor seleccionado
    id_proveedor = self.ids.spinner_proveedor.text
    id_categoria = self.ids.spinner_categoria.text
    ubicacion = self.ids.ubicacion_input.text
    barcode = self.ids.barcode_input.text

    if not self.image_blob:
        self.ids.resultado_label.text = 'Por favor, seleccione una imagen.'
        return

    # Leer la imagen seleccionada
    with open(self.image_blob[0], 'rb') as image_file:
        image_blob = image_file.read()

    try:
        insertar_producto
        self.ids.resultado_label.text = 'Producto agregado exitosamente'

    except mysql.connector.Error as err:
        self.ids.resultado_label.text = f'Error: {err}'
    finally:
        cursor.close()
        conexion.close()



def cargar_productos_completos(self, mostrar="disponibles"):
    conexion = mysql.connector.connect(database= "negocio", user="root")
    cursor = conexion.cursor()
    """Carga productos según el filtro proporcionado."""
    try:
        if mostrar == "disponibles":
            cursor.execute("SELECT nombre_producto, desc_producto, stock, barcode, estado_producto, image_blob FROM productos WHERE estado_producto = 1")
        elif mostrar == "no_disponibles":
            cursor.execute("SELECT nombre_producto, desc_producto, stock, barcode, estado_producto, image_blob FROM productos WHERE estado_producto = 0")
        else:
            cursor.execute("SELECT nombre_producto, desc_producto, stock, barcode, estado_producto , image_blob FROM productos")
        
        productos = cursor.fetchall()
        return productos
    except mysql.connector.Error as err:
        print(f"Error al cargar productos: {err}")
        return []

def cambiar_estado_producto_a_no_disponible(barcode):
    conexion = mysql.connector.connect(database= "negocio", user="root")
    cursor = conexion.cursor()
    try:
        cursor.execute("UPDATE productos SET estado_producto = 0 WHERE barcode = %s", (barcode,))
        conexion.commit()  # Asegura que se guarden los cambios
        print("Producto marcado como no disponible.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar el estado del producto: {err}")




        
