'''

Area de un rectángulo
Pide la entrada del ancho y profundo de la habitación en metros. Devuelve la superficie en metros cuadrados y en yardas cuadradas (tomando la referencia de aquí).

Restricciones
Mantener los cálculos separados de la salida
Usa una constante para las conversiones de unidades (aquí)

1 yarda (yd) = 3 ft = 91.44 cm = 0.914 m
1 yarda cuadrada (sq yd o yd²) = 9 ft² = 0,83612736 m²

'''

#CONSTANTES
conversor = 0.836

#Entradas de datos:
length = ''
weigth = ''

while length == '':
    length = input('¿Cual es el ancho de la habitación? ')
    try:
        length = float(length)
    except:
        print('El valor', length, 'no es valido. Por favor introduzca un numero') 
        length = ''
        

while weigth == '':
    weigth = input('¿Cual es la profundidad de la habitación? ')
    try:
        weigth = float(weigth)
    except:
        print('El valor', weigth, 'no es valido. Por favor introduzca un numero') 
        weigth = ''

#Calculos

def area(l, w):
    area_meters = l * w
    area_yards = area_meters / conversor 
    return print("Tu habitación mide {:.2f} metros cuadrados y {:.2f} yardas cuadradas".format(area_meters, area_yards))

area(length, weigth)



'''
#SOLUCION DRIVE

METROS_YARDA = 0.9144

longitud = float(input("¿Longitud de la habitación en metros? "))
profundo = float(input("¿Profundo de la habitación en metros? "))

s_metros = longitud * profundo
s_yardas = longitud * profundo / METROS_YARDA ** 2

print(f"Superficie de la habitación en metros cuadrados: {s_metros}")
print(f"Superficie de la habitación en yardas cuadradas: {s_yardas}")
'''