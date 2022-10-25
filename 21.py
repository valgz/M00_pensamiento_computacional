'''Maximo valor'''

num1 = ""
num2 = ""
num3 = ""

while num1 == "":
    try:
        num1 = input('Introduce un numero: ')
        num1 = float(num1)
        if num1 == num2 or num1 == num3:
            print(f"El valor \"{num1}\" no es valido. Vuelva a intentarlo.")
            num1 = ""
    except:
        print(f"El valor \"{num1}\" no es valido. Vuelva a intentarlo.")
        num1 = ""


while num2 == "":
    try:
        num2 = input('Introduce un numero: ')
        num2 = float(num2)
        if num2 == num1 or num2 == num3:
            print(f"El valor \"{num2}\" no es valido. Vuelva a intentarlo.")
            num2 = ""
    except:
        print(f"El valor \"{num2}\" no es valido. Vuelva a intentarlo.")
        num2 = ""


while num3 == "":
    try:
        num3 = input('Introduce un numero: ')
        num3 = float(num3)
        if num3 == num1 or num3 == num2:
            print(f"El valor \"{num3}\" no es valido. Vuelva a intentarlo.")
            num3 = ""
    except:
        print(f"El valor \"{num3}\" no es valido. Vuelva a intentarlo.")
        num3 = ""

#PROCESO

if (num1 > num2) and (num1 > num3):
    mayor = num1
elif (num2 > num3) and (num2 > num1):
    mayor = num2
elif (num3 > num1) and (num3 > num2):
    mayor = num3

print(f'El numero mayor es {mayor}')

    
