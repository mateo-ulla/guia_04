from PIL import Image
import os

img_route = input('Ingresa la ruta de la imagen: ')

imagen = Image.open(img_route)

nombre = os.path.basename(img_route)
extension = imagen.format
res = imagen.size
cant_pix = res[0] * res[1]
print(f' ____ {nombre} ____ {extension} ____ {res} ____ {cant_pix} ____ {img_route}')
