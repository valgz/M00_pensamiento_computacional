#Entrada

peso = 0
altura = 0

while peso == 0 and altura == 0:
    try:
        peso = float(input('Indica tu peso en kg: '))
        altura = float(input('Indica tu altura en metros: '))
    except ValueError:
        print(f'El valor introducido no es valido. Vuelva a intentarlo')
        altura = 0
        peso = 0

#Proceso

imc = peso / altura ** 2
imc = round(imc, 2)

#Salida

print(f'Su indice de masa corporal es {imc}')
if 15 < imc < 18.5:
    print(f'Su peso es normal')
if imc < 15:
    print(f'Su peso esta por debajo de lo normal')
if imc > 18.5:
    print(f'Usted tiene sobrepeso')



#SOLUCION DRIVE

peso = ""
while peso == "":
  cad = input("Peso: ")
  try:
    peso = float(cad)
  except:
    peso = ""

altura = ""
while altura == "":
  cad = input("Altura: ")
  try:
    altura = float(cad)
  except:
    altura = ""

imc = peso/altura**2

print("Tu índice de masa corporal es {:.2f}".format(imc))
if imc < 18.5:
  print("Estas muy delgado, quizás deberías visitar a tu médico.")
elif imc > 15:
  print("Tienes sobrepeso, quizás deberías visitar a tu médico.")
else:
  print("Estas en tu peso ideal")
