from PIL import Image
import os

img_route = input('Ingresa la ruta de la imagen: ')

imagen = Image.open(img_route)
grayscale_image = imagen.convert("L")

nombre = os.path.basename(img_route)
carpeta = 'ImagenesFiltradas'
path = 'D:/TP de Programacion/Python/guia mapa de bits/guia_04'
full_path = os.path.join(path, carpeta)

os.makedirs(full_path, exist_ok=True)

i = 1
while True:
    if os.path.exists(os.path.join(full_path, f'{nombre}BN{i}.png')):
        i += 1
    else:
        grayscale_image.save(os.path.join(full_path, f'{nombre}BN{i}.png'))
        break
    