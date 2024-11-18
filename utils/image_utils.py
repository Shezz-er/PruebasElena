from io import BytesIO
from PIL import Image as PILImage
import tempfile
from io import BytesIO
import decimal
import tempfile
import time
from io import BytesIO
import os
import decimal

def convert_blob_to_image(image_blob):
    # Si image_blob es de tipo decimal.Decimal, lo convertimos a bytes
    if isinstance(image_blob, decimal.Decimal):
        image_blob = bytes(str(image_blob), 'utf-8')  # Convertir el decimal a bytes

    # Creamos un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        # Escribimos el contenido de image_blob en el archivo temporal
        temp_file.write(image_blob)
        temp_file_path = temp_file.name

    # Aseguramos que el archivo se cierre y esté accesible
    time.sleep(0.4)  # Esperamos 100ms para asegurarnos de que el archivo no esté siendo utilizado

    # Devolvemos la ruta del archivo temporal
    return temp_file_path
# def convert_blob_to_image(image_blob):
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
#         # # Convertir el blob a una imagen usando PIL
#         image_data = BytesIO(image_blob)
#         image = PILImage.open(image_data)
#         # Guardar la imagen temporalmente en el archivo
#         image.save(temp_file.name)
#         # # Retornar la ruta de la imagen temporal

#         return temp_file.name

# def convert_blob_to_image(image_blob):
#     # Convertir el valor Decimal a bytes (si es necesario)
#     if isinstance(image_blob, decimal.Decimal):
#         image_blob = bytes(str(image_blob), 'utf-8')  # o el tipo adecuado

#     image_data = BytesIO(image_blob)
#     return image_data
