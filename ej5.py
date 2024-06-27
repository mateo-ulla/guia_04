from PIL import Image
import os

r_img_a_marcar = input('Ingresa la ruta de la imagen a marcar: ')
r_img_de_marca = input('Ingresa la ruta de la imagen de la marca de agua: ')

posicion = input('Ingresa la posicion de la marca (1, 2, 3 o 4): ')

if not posicion.isdigit() or int(posicion) not in [1, 2, 3, 4]:
    print('La posición ingresada no es válida.')
    exit()

img_a_marcar = Image.open(r_img_a_marcar)
img_de_marca = Image.open(r_img_de_marca)

width, height = img_a_marcar.size

posiciones = {
    1: (50, 50),
    2: (width-50, 50),
    3: (50, height-50),
    4: (width-50, height-50)
}

posicion_seleccionada = int(posicion)
img_a_marcar.paste(img_de_marca, posiciones[posicion_seleccionada])

i = 1
while True:
    if os.path.exists(f'img_marcada{i}.jpg'):
        i += 1
    else:
        img_a_marcar.save(f'img_marcada{i}.jpg')
        break