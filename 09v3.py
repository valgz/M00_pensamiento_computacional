"""VERSION PARA HABITACIÓN EN FORMA DE L"""


from math import ceil

#CONSTANTE

BOTE_METROS = 20 #Con 1 bote pintas 20 m2.

#ENTRADA

ancho = float(input('Ingresa el ancho del techo: '))
profundidad = float(input('Ingresa la profundidad del techo: '))

#CALCULO

area_g = ancho * profundidad
area_p = (ancho / 2) * (profundidad / 2)

area_l = area_g - area_p

num_litros = area_l / BOTE_METROS 
num_botes = ceil(num_litros / 5)

#SALIDA

print(f'Para pintar {area_l} m2 de techo necesitará {num_litros} litros de pintura. ')
if num_botes == 1:
    print(f'Debe comprar {num_botes} bote.')
else:
    print(f'Debe comprar {num_botes} botes.')
