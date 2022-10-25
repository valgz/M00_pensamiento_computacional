'''Conversión de divisas
Crear un programa que pase de dolares a euros. 
El programa pedirá la tasa de cambio de dolares a euros (cuantos euros se necesitan para tener un dolar). 
El programa debe devolver lo siguiente.

X dolares a una tasa de cambio de Y
Total €

Restricciones
Asegúrate de que la entrada se redondea al centavo
Utiliza una única sentencia de salida'''

#ENTRADA

#pedir tasa de cambio dolar a euro
tasa_cambio = float(input('Indique la tasa de cambio (dolar a euro): '))
#pedir total a convertir
cantidad = float(input('Inque la cantidad de dolares a convertir: '))


#SALIDA 

print("{:.2f} a una tasa de cambio de {:.2f} \n Total: {:.2f} €".format(cantidad, tasa_cambio, cantidad * tasa_cambio))


#SOLUCION DRIVE

strDolares = input("Dolares: ")
strTasa = input("Valor de cambio Dolar a Euro: ")

dolares = round(float(strDolares), 2)
tasa = float(strTasa)

euros = round(dolares * tasa, 2)

print("{} dolares a una tasa de intercambio {}\n{} €".format(dolares, tasa, euros))
