from PIL import Image
import os

img_route = input('Ingresa la ruta de la imagen: ')

angulo = input('Ingresa el ángulo de rotación para la imagen: ')

imagen = Image.open(img_route)
nombre = os.path.splitext(os.path.basename(img_route))[0]
extension = imagen.format

img_rotada = imagen.rotate(int(angulo))

img_rotada.show()

img_rot_saved = img_rotada.save(f'{nombre}_rot{angulo}º.{extension}')