'''Cálculo de interés simple
Crear un programa que calcule el interés simple, teniendo en cuenta que se calcula con la siguiente fórmula:

𝐴 = 𝑃·(1+ 𝑟𝑡 )

donde A es la cantidad ganada, P la cantidad invertida, r el interes y t los años transcurridos desde el inicio de la inversión

Tras X años de inversión al Y %, su cantidad debe ser T

Restricciones
La tasa de interés debe introducirse como porcentaje y no decimal, es decir 15 y no 0,15
La inversión debe redondearse al céntimo
La salida debe formatearse como divisa (€)'''



#ENTRADA

investment = float(input('¿Cuanto ha invertido? '))

interest_rate = ''
while interest_rate == '':
    try:
        interest_rate = float(input('¿Cual es la tasa de interés? '))
        if interest_rate < 1:
            print('Por favor introduza la tasa de interés en porcentaje. Ejemplo: 15')
            interest_rate = ''    
    except ValueError:
        print(f'El valor {interest_rate} no es valido. Vuelva a intentarlo')

years = float(input('¿Cuantos años han transcurrido? '))

#PROCESO

investment = round(investment, 2)

simple_interest = investment * (1 + ((interest_rate / 100) * years))
simple_interest = round(simple_interest, 2)

#SALIDA

print("Tras {} años de inversion al {} %, su cantidad debe ser {} €".format(years, interest_rate, simple_interest))



'''

SOLUCION DRIVE

strQ = input("Cantidad invertida: ")
strA = input("Años transcurridos: ")
strI = input("Interés anual: ")

Q = round(float(strQ), 2)
A = float(strA)
I = float(strI)/100

ganancia = Q * (1 + I * A)

print("Tras {} años de inversión al {:.2f}%, su cantidad debe ser {:.2f}€".format(A, I*100, ganancia))'''



