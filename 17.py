def conversor_temperatura(temperature, unit):
    result = 0
    if unit == "fahrenheit":
        result = str(temperature) + ' Fahrenheit son ' + str(round(((temperature - 32) * 5 / 9), 2)) + ' grados Celsius.'
    elif unit == "celsius":
        result = str(temperature) + ' Celsius son ' + str(round(((temperature * 9 / 5) + 32), 2)) + ' grados Fahrenheit.'
    return result

#ENTRADA

#pide temperatura
temperatura = float(input('Temperatura: '))
#pide unidad (celsius o farenheit)
unidad = str(input('Celsius o Fahrenheit: '))
unidad = unidad.lower()

print(conversor_temperatura(temperatura, unidad))



#SOLUCION DRIVE
'''
strTipo = input("Temperatura de entrada en Fahrenheit o Celsius (F/C)")
strTemp = input("Valor de la temperatura: ")

temp = float(strTemp)

if strTipo == 'c' or strTipo == 'C':
  strIN = 'C'
  strOUT = 'F'
  output = (temp * 9/5) + 32
else:
  strIN = 'F'
  strOUT = 'C'
  output = (temp - 32) * 5/9
  
print("\n{}º{} son {}º{}".format(temp, strIN, output, strOUT))
'''
