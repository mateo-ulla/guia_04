from PIL import Image
import os

img_route = input('Ingresa la ruta de la imagen: ')
cordenadax = int(input('Ingresa la coordenada X inicial: '))
cordenaday = int(input('Ingresa la coordenada y inicial: '))
ancho = int(input('Ingresa el ancho: '))
altura = int(input('Ingresa la altura: '))

imagen = Image.open(img_route)

nombre = 'RECORTES'
path = 'D:\TP de Programacion\Python\guia mapa de bits\guia_04'
full_path = os.path.join(path, nombre)

os.makedirs(full_path, exist_ok=True)

croppedIm = imagen.crop((cordenadax, cordenaday, ancho, altura))

i = 1
while True:
    if os.path.exists(os.path.join(full_path, f'recorte{i}.png')):
        i += 1
    else:
        croppedIm.save(os.path.join(full_path, f'recorte{i}.png'))
        break
    