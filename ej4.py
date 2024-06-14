from PIL import Image
import os

img_route = input('Ingresa la ruta de la imagen: ')
cordenadax = int(input('Ingresa la coordenada X inicial: '))
cordenaday = int(input('Ingresa la coordenada y inicial: '))
ancho = int(input('Ingresa el ancho: '))
altura = int(input('Ingresa la altura: '))

imagen = Image.open(img_route)

nombre = 'RECORTES'
path = '\\institutodc01\d46766768\Python\guia04'
full_path = os.path.join(path, nombre)

os.makedirs(full_path, exist_ok=True)

croppedIm = imagen.crop((cordenadax, cordenaday, ancho, altura))

for i in range(1, 100):        
    if(os.path.exists(f'recorte{i}.png')):
        croppedIm.save(f'recorte{i+1}.png')
        break
    else:
        croppedIm.save('recorte1.png')