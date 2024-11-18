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

conexion = mysql.connector.connect(database= "negocio", user="root")
cursor = conexion.cursor()


def cambiar_estado_producto_a_no_disponible(barcode):
    """Cambia el estado de un producto a no disponible en la base de datos."""
    try:
        cursor.execute("UPDATE productos SET estado_producto = 0 WHERE barcode = %s", (barcode,))
        conexion.commit()  # Asegura que se guarden los cambios
        print("Producto marcado como no disponible.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar el estado del producto: {err}")


