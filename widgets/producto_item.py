from utils.db_utils import *

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from utils.image_utils import convert_blob_to_image
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
from kivy.graphics import Color, Rectangle
from kivy import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class ProductoItem(BoxLayout):
    def __init__(self, nombre_producto, desc_producto, stock, fecha_vencimiento, barcode, estado_producto, image_blob, view_product_screen, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = 10
        self.spacing = 10
        self.size_hint = (1, None)  # Full width but fixed height
        self.height = '160dp'  # Fixed height to maintain consistent item size

        self.barcode = barcode
        self.estado_producto = estado_producto


        self.view_product_screen = view_product_screen  # Referencia a ViewProductScreen


        # Background color for visibility
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 0.5)  # Light gray background with some transparency
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Product image
        image_path = convert_blob_to_image(image_blob)
        self.add_widget(Image(source=image_path, size_hint=(None, None), size=('70dp', '70dp')))

        # Product details
        info_layout = BoxLayout(orientation='vertical', size_hint=(0.6, 1))
        info_layout.add_widget(Label(text=f"Producto: {nombre_producto}", color=(0, 0, 0, 1), font_size='12sp'))
        info_layout.add_widget(Label(text=f"Descripción: {desc_producto}", color=(0, 0, 0, 1), font_size='12sp'))
        info_layout.add_widget(Label(text=f"Stock: {stock}", color=(0, 0, 0, 1), font_size='12sp'))
        info_layout.add_widget(Label(text=f"Fecha Vencimiento: {fecha_vencimiento}", color=(0, 0, 0, 1), font_size='12sp'))

        info_layout.add_widget(Label(text=f"Código de Barra: {barcode}", color=(0, 0, 0, 1), font_size='12sp'))
        info_layout.add_widget(Label(text=f"Estado producto: {estado_producto}", color=(0, 0, 0, 1), font_size='12sp'))

        self.add_widget(info_layout)

        # Buttons for edit and delete
        button_layout = BoxLayout(orientation='vertical', spacing=5, size_hint=(None, None), width='80dp')
        button_layout.size_hint_x = 0.25  # Limit button layout width to prevent overflow

        # Edit button
        edit_button = Button(text='Editar', size_hint_x=None, width='70dp', font_size='10sp', background_color=(0.2, 0.6, 1, 1))
        edit_button.bind(on_press=lambda x: self.editar_producto(nombre_producto, desc_producto, stock, fecha_vencimiento, barcode, estado_producto))
        button_layout.add_widget(edit_button)

        # Delete button
        delete_button = Button(text='Eliminar', size_hint_x=None, width='70dp', font_size='10sp', background_color=(1, 0.2, 0.2, 1))
        delete_button.bind(on_press=self.confirmar_eliminacion)

        button_layout.add_widget(delete_button)

        self.add_widget(button_layout)


    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


    def confirmar_eliminacion(self, instance):
            # Crear popup de confirmación
            popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
            popup_layout.add_widget(Label(text="¿Está seguro de que desea marcar este producto como no disponible?"))

            # Botones para confirmar o cancelar
            botones_layout = BoxLayout(size_hint_y=None, height='50dp', spacing=10)
            boton_si = Button(text="Sí", background_color=(0.2, 0.6, 1, 1))
            boton_no = Button(text="No", background_color=(1, 0.2, 0.2, 1))
            
            botones_layout.add_widget(boton_si)
            botones_layout.add_widget(boton_no)
            popup_layout.add_widget(botones_layout)

            # Crear el popup
            popup = Popup(
                title="Confirmar",
                content=popup_layout,
                size_hint=(None, None),
                size=('400dp', '200dp')
            )

            # Bind para cerrar el popup y ejecutar la función de cambio de estado si se confirma
            boton_si.bind(on_press=lambda x: self.marcar_como_no_disponible(popup))
            boton_no.bind(on_press=popup.dismiss)

            popup.open()

    def marcar_como_no_disponible(self, popup):
        # Cambia el estado del producto a no disponible en la base de datos y cierra el popup
        cambiar_estado_producto_a_no_disponible(self.barcode)
        popup.dismiss()

        # Opcional: refrescar la vista para actualizar el grid de productos
        self.view_product_screen.cargar_productos_completos()



    # def confirmar_eliminacion(self, instance):
    #         # Crear popup de confirmación
    #         popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    #         popup_layout.add_widget(Label(text="¿Está seguro de que desea marcar este producto como no disponible?"))

    #         # Botones para confirmar o cancelar
    #         botones_layout = BoxLayout(size_hint_y=None, height='50dp', spacing=10)
    #         boton_si = Button(text="Sí", background_color=(0.2, 0.6, 1, 1))
    #         boton_no = Button(text="No", background_color=(1, 0.2, 0.2, 1))
            
    #         botones_layout.add_widget(boton_si)
    #         botones_layout.add_widget(boton_no)
    #         popup_layout.add_widget(botones_layout)

    #         # Crear el popup
    #         popup = Popup(
    #             title="Confirmar",
    #             content=popup_layout,
    #             size_hint=(None, None),
    #             size=('400dp', '200dp')
    #         )

    #         # Bind para cerrar el popup y ejecutar la función de cambio de estado si se confirma
    #         boton_si.bind(on_press=lambda x: self.marcar_como_no_disponible(popup))
    #         boton_no.bind(on_press=popup.dismiss)

    #         popup.open()

    # def marcar_como_no_disponible(self, popup):
    #     # Cambia el estado del producto a no disponible en la base de datos y cierra el popup
    #     cambiar_estado_producto_a_no_disponible(self.barcode)
    #     popup.dismiss()

    #     # Opcional: refrescar la vista para actualizar el grid de productos
    #     self.parent.parent.parent.cargar_productos_completos()











# class ProductoItem(BoxLayout):
#     def __init__(self, nombre_producto, desc_producto, stock, barcode, image_blob, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = 'horizontal'
#         self.padding = 10
#         self.spacing = 10
#         self.size_hint = (1, None)  # Full width but fixed height
#         self.height = '160dp'  # Fixed height to maintain consistent item size

#         self.barcode = barcode

#         # Background color for visibility
#         with self.canvas.before:
#             Color(0.9, 0.9, 0.9, 0.5)  # Light gray background with some transparency
#             self.rect = Rectangle(size=self.size, pos=self.pos)
#         self.bind(size=self.update_rect, pos=self.update_rect)

#         # Product image
#         image_path = convert_blob_to_image(image_blob)
#         self.add_widget(Image(source=image_path, size_hint=(None, None), size=('70dp', '70dp')))

#         # Product details
#         info_layout = BoxLayout(orientation='vertical', size_hint=(0.6, 1))
#         info_layout.add_widget(Label(text=f"Producto: {nombre_producto}", color=(0, 0, 0, 1), font_size='12sp'))
#         info_layout.add_widget(Label(text=f"Descripción: {desc_producto}", color=(0, 0, 0, 1), font_size='12sp'))
#         info_layout.add_widget(Label(text=f"Stock: {stock}", color=(0, 0, 0, 1), font_size='12sp'))
#         info_layout.add_widget(Label(text=f"Código de Barra: {barcode}", color=(0, 0, 0, 1), font_size='12sp'))
#         self.add_widget(info_layout)

#         # Buttons for edit and delete
#         button_layout = BoxLayout(orientation='vertical', spacing=5, size_hint=(None, None), width='80dp')
#         button_layout.size_hint_x = 0.25  # Limit button layout width to prevent overflow

#         # Edit button
#         edit_button = Button(text='Editar', size_hint_x=None, width='70dp', font_size='10sp', background_color=(0.2, 0.6, 1, 1))
#         edit_button.bind(on_press=lambda x: self.editar_producto(nombre_producto, desc_producto, stock, barcode))
#         button_layout.add_widget(edit_button)

#         # Delete button
#         delete_button = Button(text='Eliminar', size_hint_x=None, width='70dp', font_size='10sp', background_color=(1, 0.2, 0.2, 1))
#         delete_button.bind(on_press=lambda x: self.pop_warning(barcode))
#         button_layout.add_widget(delete_button)

#         self.add_widget(button_layout)

#     def update_rect(self, *args):
#         self.rect.size = self.size
#         self.rect.pos = self.pos


#     def pop_warning(self, barcode):
#         # Mostrar un popup de confirmación
#         content = BoxLayout(orientation='vertical')
#         content.add_widget(Label(text='¿Estás seguro de que quieres eliminar este producto?'))
        
#         btn_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp')
        
#         confirm_button = Button(text='Eliminar', size_hint_x=None, width='100dp')
#         cancel_button = Button(text='Cancelar', size_hint_x=None, width='100dp')
        
#         btn_layout.add_widget(confirm_button)
#         btn_layout.add_widget(cancel_button)
        
#         content.add_widget(btn_layout)
        
#         popup = Popup(title='Confirmar Eliminación', content=content, size_hint=(0.6, 0.3))
        
#         def confirm_action(instance):
#             popup.dismiss()  # Cierra el pop-up
            
#             # Actualizar la vista
#             screen_manager = App.get_running_app().root
#             view_screen = screen_manager.get_screen('view_product_screen')
#             view_screen.cargar_productos_completos()  # Recarga los productos en el grid
        
#         confirm_button.bind(on_press=confirm_action)
#         cancel_button.bind(on_press=popup.dismiss)  # Cerrar el popup sin hacer nada
        
#         popup.open()  # Mostrar el popup
        
#     def eliminar_producto(self, barcode):
#         screen_manager = App.get_running_app().root
#         view_screen = screen_manager.get_screen('view_product_screen')
#         productos_grid = view_screen.ids.productos_grid  # Obtener el grid de productos
        
#         # Verificar que el grid no esté vacío y tenga productos
#         if not productos_grid.children:
#             print("El grid está vacío. No se puede eliminar el producto.")
#             return
        
#         # Buscar y eliminar el widget que contiene el producto con el barcode dado
#         for widget in productos_grid.children[:]:  # Iterar sobre una copia de la lista de hijos del grid
#             # Verificar que el widget es un ProductoItem y que tiene el atributo barcode
#             if isinstance(widget, ProductoItem) and hasattr(widget, 'barcode') and widget.barcode == barcode:
#                 productos_grid.remove_widget(widget)  # Eliminar el widget del grid
#                 print(f"Producto con barcode {barcode} eliminado.")
#                 break  # Salir una vez que se encuentra y elimina el producto
#             else:
#                 print(f"No se encontró un ProductoItem con barcode {barcode}.")
    
#         view_screen.cargar_productos_completos()



    def editar_producto(self, nombre_producto, desc_producto, stock, fecha_vencimiento, barcode, estado_producto):
        # Crear un popup para editar el producto
        popup = Popup(title='Editar Producto', size_hint=(None, None), size=(400, 400))

        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        nombre_input = TextInput(text=nombre_producto, hint_text="Nombre del Producto")
        desc_input = TextInput(text=desc_producto, hint_text="Descripción")
        stock_input = TextInput(text=str(stock), hint_text="Stock", input_filter='int')
        fecha_input = TextInput(text=fecha_vencimiento, hint_text="Fecha de Vencimiento")
        barcode_input = TextInput(text=str(barcode), hint_text="Código de Barra")
        estado_input = TextInput(text=str(estado_producto), hint_text="Estado del producto", input_filter='int')

        content.add_widget(Label(text="Editar Producto"))
        content.add_widget(nombre_input)
        content.add_widget(desc_input)
        content.add_widget(stock_input)
        content.add_widget(fecha_input)
        content.add_widget(barcode_input)
        content.add_widget(estado_input)


        # Botón para guardar cambios
        save_button = Button(text='Guardar')
        save_button.bind(on_press=lambda x: self.guardar_cambios(popup, nombre_input.text, desc_input.text, stock_input.text, fecha_input.text, barcode_input.text, estado_input.text))

        content.add_widget(save_button)
        popup.content = content
        popup.open()


    def guardar_cambios(self, popup, nombre_producto, desc_producto, stock, fecha_vencimiento, barcode, estado_producto):
        try:
            # Conectar a la base de datos
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="negocio"
            )
            cursor = db.cursor()

            # Actualizar el producto en la tabla 'productos'
            query_producto = """UPDATE productos 
                                SET nombre_producto = %s, desc_producto = %s, stock = %s, estado_producto = %s
                                WHERE barcode = %s"""
            cursor.execute(query_producto, (nombre_producto, desc_producto, stock, estado_producto, barcode))
            
            # Confirmar cambios para 'productos'
            db.commit()

            # Verificar si se actualizó algún registro en 'productos'
            if cursor.rowcount > 0:
                # Obtener el ID del producto para usarlo en la tabla 'productos_vencimientos'
                cursor.execute("SELECT id_producto FROM productos WHERE barcode = %s", (barcode,))
                id_producto = cursor.fetchone()

                if id_producto:
                    id_producto = id_producto[0]  # Extraer el valor del ID

                    # Insertar o actualizar en 'productos_vencimientos'
                    query_vencimiento = """
                        INSERT INTO productos_vencimientos (id_producto, fecha_vencimiento)
                        VALUES (%s, %s)
                        ON DUPLICATE KEY UPDATE fecha_vencimiento = VALUES(fecha_vencimiento)
                    """
                    cursor.execute(query_vencimiento, (id_producto, fecha_vencimiento))

                    # Confirmar cambios para 'productos_vencimientos'
                    db.commit()

                self.show_success_popup()  # Mostrar popup de éxito
            else:
                self.show_error_popup("No se encontró el producto para actualizar")

        except Exception as e:
            print(f"Error al actualizar el producto: {e}")
            self.show_error_popup("Ocurrió un error al guardar los cambios.")
        finally:
            # Cerrar la conexión con la base de datos
            cursor.close()
            db.close()

            # Cierra el popup después de guardar
            popup.dismiss()
            screen_manager = App.get_running_app().root

            # Obtener la instancia de la pantalla 'view_product_screen' y llamar a cargar_productos()
            view_screen = screen_manager.get_screen('view_product_screen')
            view_screen.cargar_productos_completos()



    # def guardar_cambios(self, popup, nombre_producto, desc_producto, stock, fecha_vencimiento, barcode, estado_producto):
    #     try:
    #         # Conectar a la base de datos
    #         db = mysql.connector.connect(
    #             host="localhost",
    #             user="root",
    #             password="",
    #             database="mydb"
    #         )
    #         cursor = db.cursor()

    #         # Actualizar el producto en la base de datos
    #         query = """UPDATE productos 
    #                 SET nombre_producto = %s, desc_producto = %s, stock = %s,
    #                 WHERE barcode = %s"""
    #         cursor.execute(query, (nombre_producto, desc_producto, stock, fecha_vencimiento, barcode))
            
    #         # Confirmar cambios en la base de datos
    #         db.commit()

    #         # Verificar si la actualización fue exitosa
    #         if cursor.rowcount > 0:
    #             self.show_success_popup()  # Mostrar popup de éxito
    #         else:
    #             self.show_error_popup("No se encontró el producto para actualizar")

    #     except Exception as e:
    #         print(f"Error al actualizar el producto: {e}")
    #     finally:
    #         # Cerrar la conexión con la base de datos
    #         cursor.close()
    #         db.close()

    #         # Cierra el popup después de guardar
    #         popup.dismiss()
    #         screen_manager = App.get_running_app().root

    #         # Obtener la instancia de la pantalla 'view_product_screen' y llamar a cargar_productos()
    #         view_screen = screen_manager.get_screen('view_product_screen')
    #         view_screen.cargar_productos() 

    def show_success_popup(self):
            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text='Producto editado con éxito!'))
            close_button = Button(text='Cerrar', size_hint_y=None, height='40dp')
            content.add_widget(close_button)
            
            popup = Popup(title='Éxito', content=content, size_hint=(0.6, 0.3))
            close_button.bind(on_press=popup.dismiss)
            popup.open()
        
    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        close_button = Button(text='Cerrar', size_hint_y=None, height='40dp')
        content.add_widget(close_button)
        
        popup = Popup(title='Error', content=content, size_hint=(0.6, 0.3))
        close_button.bind(on_press=popup.dismiss)
        popup.open()
