from kivy.uix.screenmanager import Screen
from utils.db_utils import obtener_opciones, insertar_producto
from utils.image_utils import convert_blob_to_image

class AddProductScreen(Screen):
    def on_enter(self):
        self.on_start()

    def on_start(self):
        self.ids.spinner_medida.values = obtener_opciones("SELECT nombre_medida FROM unidad_medida")
        self.ids.spinner_proveedor.values = obtener_opciones("SELECT nombre_proveedor FROM proveedores")
        self.ids.spinner_categoria.values = obtener_opciones("SELECT nombre_categoria FROM categoria")

    # def agregar_producto(self):
    #     # Código para agregar el producto usando `insertar_producto`