"""VERSION PARA HABITACIÓN CIRCULAR"""


from math import ceil
from cmath import pi

#CONSTANTE

BOTE_METROS = 20 #Con 1 bote pintas 20 m2.

#ENTRADA

radio = float(input('Ingresa el radio de la habitación: '))

#CALCULO

area = round((pi * radio ** 2), 2)
num_litros = round((area / BOTE_METROS), 2) 
num_botes = ceil(num_litros / 5)

#SALIDA

print(f'Para pintar {area} m2 de techo necesitará {num_litros} litros de pintura. Debe comprar {num_botes} botes.')

