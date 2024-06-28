from PIL import Image
import os

img_route = input('Ingresa la ruta de las imagenes: ')
img_width = int(input('Ingresa el ancho del collage: '))
img_height = int(input('Ingresa el alto del collage: '))

rutas = []

for f in os.listdir(img_route): 
        rutas.append(os.path.join(img_route, f))

if not len(rutas) == 9:
        print("Debe contener 9 imagenes")
        exit()

miniaturas = []         
for i in rutas:
        Img = Image.open(i)
        Img.thumbnail((img_width // 3, img_height // 3))
        miniaturas.append(Img)
        
collage = Image.new('RGB', (img_width, img_height))

index = 0
for top in range(0, img_height, miniaturas[0].height):
        for left in range(0, img_width, miniaturas[0].width):
                collage.paste(miniaturas[index], (left, top))
                index += 1
                if index >= len(miniaturas):
                        break
        if index >= len(miniaturas):
                break

i = 1
while True:
        if os.path.exists(f'collage{i}.jpg'):
                i += 1
        else:
                collage.save(f'collage{i}.jpg')
                break
