'''Pintando el techo

5 litros de pintura dan para pintar 100 metros cuadrados de techo. 
Teniendo esto en cuenta haz un programa que diga cuantos botes de 5 litros de pintura 
hay que comprar para pintar un techo de anchura y profundidad informada por el usuario (en metros). 
Devuelve el número de botes suficiente y por supuesto en números enteros.

Necesitarás 12 litros para pintar 240 metros cuadrados de techo.

Debes comprar 3 botes de pintura.

Restricciones

Utiliza una constante para calcular la conversión botes de pintura/metros de techo
Asegurate de comprar un número entero de botes de pintura suficiente (el siguiente número entero) pero no de más'''



from math import ceil

#CONSTANTE

BOTE_METROS = 20 #Con 1 bote pintas 20 m2.

#ENTRADA

ancho = float(input('Ingresa el ancho del techo: '))
profundidad = float(input('Ingresa la profundidad del techo: '))

#CALCULO

area = ancho * profundidad
num_litros = area / BOTE_METROS 
num_botes = ceil(num_litros / 5)

#SALIDA

print(f'Para pintar {area} m2 de techo necesitará {num_litros} litros de pintura. Debe comprar {num_botes} botes.')



#SOLUCION DRIVE

tasalitros = 0.05

strLon = input("Ancho del techo: ")
strProf = input("Profundo del techo: ")

lon = float(strLon)
prof = float(strProf)

area = lon * prof

litros = area * tasalitros
botes = litros // 5
#Con // calculas el cociente entero de una división.

botes += 1 if litros % 5 > 0 else 0

print("Necesitarás {} litros para pintar {} metros cuadrados de techo.".format(round(litros,2), round(area, 2)))
print("Debes comprar {} botes de pintura".format(botes))

