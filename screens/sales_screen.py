from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from screens.view_product_screen import *
from widgets import *
from widgets.producto_item import ProductoItem
from PIL import Image as PILImage
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from screens.view_product_screen import ViewProductScreen 
from database import *

conexion = mysql.connector.connect(database= "negocio", user="root")
cursor = conexion.cursor()

# screens/sales_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from utils import *
from database import *

class SalesScreen(Screen):
    def __init__(self, **kwargs):
        super(SalesScreen, self).__init__(**kwargs)
        self.conexion = obtener_conexion()  # Conexión a la base de datos
        self.cursor = self.conexion.cursor()
        self.productos = []  # Inicializa la lista de productos
        # self.cargar_productos_y_mostrar()

#     def cargar_productos_y_mostrar(self):
#         # Llama a cargar_productos para obtener los productos desde la base de datos
#         self.productos = cargar_productos(self.cursor)
        
#         # Accede al GridLayout en el KV para agregar los productos
#         productos_grid = self.ids.productos_grid  # Asegúrate de que este ID esté en el archivo KV
#         productos_grid.clear_widgets()  # Limpia los widgets previos si hay

#         # Agrega cada producto como un nuevo Label al GridLayout
#         for producto in self.productos:
#             # Aquí asumimos que cada producto es una tupla con (id, nombre, precio, ...)
#             item = Label(text=str(producto[1]) if producto[1] is not None else "")  # Asegura que el texto sea un str
#             productos_grid.add_widget(item)

#     def on_leave(self):
#         # Cierra la conexión cuando se salga de la pantalla
#         self.cursor.close()
#         self.conexion.close()



# ///////////////////////////////////////////////




# class SalesScreen(Screen):

#     # def __init__(self, **kwargs):
#     #     super(SalesScreen, self).__init__(**kwargs)
#     #     self.productos = []  # Inicializa la lista de productos
#     #     self.view_product_screen = ViewProductScreen()  # Crea una instancia de ViewProductScreen
#     #     self.cargar_productos()  # Llama al método cargar_productos de ViewProductScreen

#     # def cargar_productos(self):
#     #     # Llamar a la función que has importado desde productos.py
#     #     self.view_product_screen.cargar_productos() 

#     def __init__(self, **kwargs):
#         super(SalesScreen, self).__init__(**kwargs)
#         conexion = obtener_conexion()
#         self.cursor = conexion.cursor()
#         self.productos = self.cargar_productos()  # Carga los productos al iniciar

#     def cargar_productos(self):
#         # Usa cargar_productos directamente con el cursor de SalesScreen
#         productos = cargar_productos(self.cursor)
#         return productos

#     def filtrar_productos(self, texto_busqueda):
#         # Filtrar productos que coincidan con el texto ingresado
#         productos_filtrados = [p for p in self.productos if texto_busqueda.lower() in p[0].lower()]

#         productos_grid = self.ids.productos_grid
#         productos_grid.clear_widgets()

#         for producto in productos_filtrados:
#             nombre_producto, precio = producto

#             boton_producto = Button(text=f'{nombre_producto} - ${precio}')
#             boton_producto.size_hint_y = None
#             boton_producto.height = '40dp'
#             boton_producto.bind(on_press=lambda x, nombre=nombre_producto, p=precio: self.agregar_al_resumen(nombre, p))
#             productos_grid.add_widget(boton_producto)

#         # Ajustar el tamaño del GridLayout de productos
#         productos_grid.height = len(productos_filtrados) * 80


#     def crear_callback(self, nombre_producto, precio_venta):
#         # Esta función devuelve otra función que es el callback real
#         def callback(instance):
#             print(f"Producto seleccionado: {nombre_producto}, Precio: {precio_venta}")
#             self.agregar_al_resumen(nombre_producto, precio_venta)
#         return callback

#     def agregar_al_resumen(self, nombre_producto, precio_venta):
#         # Este print es útil para depuración
#         print(f"Agregando al resumen: {nombre_producto}, Precio: {precio_venta}")
        
#         # Obtener el GridLayout del resumen
#         resumen_grid = self.ids.resumen_grid

#         # Crear una nueva etiqueta para el producto seleccionado
#         label = Label(text=f'{nombre_producto} - ${precio_venta}', size_hint_y=None, height='40dp')
#         resumen_grid.add_widget(label)

#         # Actualizar el total de la compra
#         try:
#             # Aseguramos que el total se convierta en un float para poder sumar correctamente
#             total_actual = float(self.ids.total_label.text)
#             nuevo_total = total_actual + float(precio_venta)
#             self.ids.total_label.text = str(nuevo_total)
#         except Exception as e:
#             print(f"Error al actualizar el total: {e}")

#         # Ajustar el tamaño del GridLayout del resumen
#         resumen_grid.height = len(resumen_grid.children) * 80

#     def calcular_vuelto(self):
#         # Obtener el total de la compra
#         total = float(self.ids.total_label.text)

#         # Obtener el monto que pagó el cliente
#         pago_cliente = float(self.ids.pago_cliente.text)

#         # Calcular el vuelto
#         if pago_cliente >= total:
#             vuelto = pago_cliente - total
#             self.ids.vuelto_label.text = f'Vuelto: ${vuelto}'
#         else:
#             self.ids.vuelto_label.text = 'Pago insuficiente'