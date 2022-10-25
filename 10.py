'''Aplicando impuestos
Haz un programa que aplique un impuesto de 5,5% sobre tres precios introducidos por el usuario. 
Deben introducirse también el número de ejemplares de producto de cada precio que se compran. 
Se debe imprimir el subtotal sin tasas, la tasa y la suma de ambos

Restricciones
Manten separadas las partes de entrada, salida y proceso de tu programa'''



from mod_10 import *

#ENTRADA

#pedir primer precio y num productos
precio1 = float(input('Indique el precio: '))
ejemplares1 = int(input('Indique la cantidad de ejemplares: '))

#pedir segundo precio y num productos
precio2 = float(input('Indique el precio: '))
ejemplares2 = int(input('Indique la cantidad de ejemplares: '))

#pedir tercer precio y num productos
precio3 = float(input('Indique el precio: '))
ejemplares3 = int(input('Indique la cantidad de ejemplares: '))

#PROCESO

precios = [precio1, precio2, precio3]
ejemplares = [ejemplares1, ejemplares2, ejemplares3]


subtotales = calcula_subtotal(precios, ejemplares) 
tasas = calcula_tasa_impuesto(precios)
totales = calcula_total(subtotales, tasas, ejemplares)


subtotal = sum(subtotales)
total = sum(totales)
tasa = sum(tasas)

#SALIDA

print("Subtotales\t Tasas \t Totales")

indice = 0
for i in range(3):
    print("{:.2f}\t \t {:.2f}\t {:.2f}".format(subtotales[indice], tasas[indice], totales[indice]))
    indice += 1
print("-------------------------------\n{:.2f} \t \t {:.2f}\t {:.2f}".format(subtotal, tasa, total))


'''
#SOLUCION DRIVE

strPrice01 = input("Precio 01: ")
strQ01 = input("Cantidad 01: ")

strPrice02 = input("Precio 02: ")
strQ02 = input("Cantidad 02: ")

strPrice03 = input("Precio 03: ")
strQ03 = input("Cantidad 03: ")

price01 = float(strPrice01)
Q01 = float(strQ01)
price02 = float(strPrice02)
Q02 = float(strQ02)
price03 = float(strPrice03)
Q03 = float(strQ03)

subtotal = 0
subtotal += price01*Q01
subtotal += price02*Q02
subtotal += price03*Q03

tax = subtotal * 5.5

total = subtotal + tax

print("Subtotal: {}".format(subtotal))
print("Tasas: {}".format(tax))
print("Total: {}".format(total))

'''
