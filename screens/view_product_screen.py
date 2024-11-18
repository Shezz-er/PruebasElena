from kivy.uix.screenmanager import Screen
from widgets import *
from widgets.producto_item import ProductoItem
import mysql.connector
from utils.db_utils import *
from utils.db_utils import cargar_productos_completos
import mysql.connector
from kivy.uix.screenmanager import Screen
from database import *

conexion = mysql.connector.connect(database="negocio", user="root")
cursor = conexion.cursor()

class ViewProductScreen(Screen):
    
    # def cargar_productos_completos(self, filtro="Mostrar disponibles"):  # Agregar filtro como argumento
    #     conexion = obtener_conexion()
    #     if conexion is None:
    #         print("Error: No se pudo establecer conexión a la base de datos.")
    #         return

    #     # Llama a cargar_productos_completos con el filtro correcto
    #     if filtro == "Mostrar disponibles":
    #         productos = cargar_productos_completos(self, mostrar="disponibles")
    #     elif filtro == "Mostrar no disponibles":
    #         productos = cargar_productos_completos(self, mostrar="no_disponibles")
    #     else:
    #         productos = cargar_productos_completos(self, mostrar="todos")

    #     # Limpia la vista de productos
    #     productos_grid = self.ids.productos_grid
    #     productos_grid.clear_widgets()

    #     # Agregar productos a la interfaz
    #     for producto in productos:
    #         nombre_producto, desc_producto, stock, barcode, estado_producto, image_blob = producto
    #         product_item = ProductoItem (
    #             nombre_producto=nombre_producto,
    #             desc_producto=desc_producto,
    #             stock=str(stock),
    #             barcode=barcode,
    #             estado_producto=str(estado_producto),
    #             image_blob=image_blob,
    #             view_product_screen=self
    #         )
    #         productos_grid.add_widget(product_item)

    #     conexion.close()


    # def cargar_productos_completos(self, filtro="Mostrar disponibles"):
    #     try:
    #         conexion = obtener_conexion()
    #         if conexion is None:
    #             print("Error: No se pudo establecer conexión a la base de datos.")
    #             return

    #         # Consulta para obtener productos con su fecha de vencimiento
    #         query = """
    #                 SELECT 
    #                 p.nombre_producto, 
    #                 p.desc_producto, 
    #                 p.stock, 
    #                 pv.fecha_vencimiento, 
    #                 p.barcode, 
    #                 p.estado_producto, 
    #                 p.image_blob
    #             FROM productos p
    #             LEFT JOIN productos_vencimientos pv ON p.id_producto = pv.id_producto
    #         """
    #         cursor.execute(query)
    #         productos = cursor.fetchall()

    #         if filtro == "Mostrar disponibles":
    #             productos = cargar_productos_completos(self, mostrar="disponibles")
    #         elif filtro == "Mostrar no disponibles":
    #             productos = cargar_productos_completos(self, mostrar="no_disponibles")
    #         else:
    #             productos = cargar_productos_completos(self, mostrar="todos")

    #         # Limpia la vista de productos
    #         productos_grid = self.ids.productos_grid
    #         productos_grid.clear_widgets()

    #         # Usar los datos en la interfaz
    #         # for producto in productos:
    #         #     nombre_producto, desc_producto, stock, fecha_vencimiento,barcode, estado_producto, image_blob = producto
    #         #     product_item = ProductoItem (
    #         #         nombre_producto=nombre_producto,
    #         #         desc_producto=desc_producto,
    #         #         stock=str(stock),
    #         #         fecha_vencimiento=fecha_vencimiento,
    #         #         barcode=barcode,
    #         #         estado_producto=str(estado_producto),
    #         #         image_blob=image_blob,
    #         #         view_product_screen=self
    #         #     )
    #         #     productos_grid.add_widget(product_item)

    #         for producto in productos:
    #             nombre_producto, desc_producto, stock, fecha_vencimiento, barcode, estado_producto, image_blob = producto
    #             product_item = ProductoItem(
    #                 nombre_producto=nombre_producto,
    #                 desc_producto=desc_producto,
    #                 stock=str(stock),
    #                 fecha_vencimiento=fecha_vencimiento,
    #                 barcode=barcode,
    #                 estado_producto=str(estado_producto),
    #                 image_blob=image_blob,
    #                 view_product_screen=self
    #         )
    #         productos_grid.add_widget(product_item)

    #     except Exception as e:
    #         print(f"Error al cargar productos: {e}")
    #     finally:
    #         cursor.close()
    #         conexion.close()

    # def cargar_productos_completos(self, filtro="Mostrar disponibles"):
    #     try:
    #         conexion = obtener_conexion()
    #         if conexion is None:
    #             print("Error: No se pudo establecer conexión a la base de datos.")
    #             return

    #         cursor = conexion.cursor()

    #         # Consulta para obtener productos con su fecha de vencimiento
    #         query = """
    #             SELECT 
    #                 p.nombre_producto, 
    #                 p.desc_producto, 
    #                 p.stock, 
    #                 pv.fecha_vencimiento, 
    #                 p.barcode, 
    #                 p.image_blob,
    #                 p.estado_producto
    #             FROM productos p
    #             LEFT JOIN productos_vencimientos pv ON p.id_producto = pv.id_producto
    #         """
    #         cursor.execute(query)
    #         productos = cursor.fetchall()

    #         # Aplicar filtro
    #         if filtro == "Mostrar disponibles":
    #             productos = cargar_productos_completos(self, mostrar="disponibles")
    #         elif filtro == "Mostrar no disponibles":
    #             productos = cargar_productos_completos(self, mostrar="no_disponibles")
    #         else:
    #             productos = cargar_productos_completos(self, mostrar="todos")


    #         # Limpia la vista de productos
    #         productos_grid = self.ids.productos_grid
    #         productos_grid.clear_widgets()

    #         # Usar los datos en la interfaz
    #         # Usar los datos en la interfaz
    #         for producto in productos:
    #             (
    #                 nombre_producto,
    #                 desc_producto,
    #                 stock,
    #                 fecha_vencimiento,
    #                 barcode,
    #                 image_blob,
    #                 estado_producto,
    #             ) = producto

    #             product_item = ProductoItem(
    #                 nombre_producto=nombre_producto,
    #                 desc_producto=desc_producto,
    #                 stock=str(stock),
    #                 fecha_vencimiento=fecha_vencimiento,
    #                 barcode=barcode,
    #                 image_blob=image_blob,
    #                 estado_producto=str(estado_producto),
    #                 view_product_screen=self,
    #             )
    #             productos_grid.add_widget(product_item)

    #     except Exception as e:
    #         print(f"Error al cargar productos: {e}")
    #     finally:
    #         if cursor:
    #             cursor.close()
    #         if conexion:
    #             conexion.close()
    def cargar_productos_completos(self, filtro="Mostrar disponibles"):
        try:
            conexion = obtener_conexion()
            if conexion is None:
                print("Error: No se pudo establecer conexión a la base de datos.")
                return

            cursor = conexion.cursor()


            # Consulta para obtener productos con manejo de valores NULL
            query = """
                SELECT 
                    p.nombre_producto, 
                    p.desc_producto, 
                    p.stock, 
                    COALESCE(pv.fecha_vencimiento, '1900-01-01') AS fecha_vencimiento, 
                    p.barcode, 
                    p.estado_producto, 
                    p.image_blob
                FROM productos p
                LEFT JOIN productos_vencimientos pv ON p.id_producto = pv.id_producto
            """
            cursor.execute(query)
            productos = cursor.fetchall()
            




            # Limpia la vista de productos
            productos_grid = self.ids.productos_grid
            productos_grid.clear_widgets()


            if filtro == "Mostrar disponibles":
                productos = [producto for producto in productos if producto[5] == 1]  # estado_producto = 1 (disponible)
            elif filtro == "Mostrar no disponibles":
                productos = [producto for producto in productos if producto[5] == 0]  # estado_producto = 0 (no disponible)
            elif filtro == "Mostrar todos":
                productos = productos




            # Usar los datos en la interfaz
            for index, producto in enumerate(productos):
                try:
                    # Intenta desempacar los valores
                    (
                        nombre_producto,
                        desc_producto,
                        stock,
                        fecha_vencimiento,
                        barcode,
                        estado_producto,
                        image_blob,
                    ) = producto
                except ValueError as e:
                    print(f"Error en la fila {index}: {producto} - {e}")
                    continue

                product_item = ProductoItem(
                    nombre_producto=nombre_producto,
                    desc_producto=desc_producto,
                    stock=str(stock),
                    fecha_vencimiento=fecha_vencimiento,
                    barcode=barcode,
                    estado_producto=str(estado_producto),
                    image_blob=image_blob,
                    view_product_screen=self,
                )
                productos_grid.add_widget(product_item)


        except Exception as e:
            print(f"Error al cargar productos: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
