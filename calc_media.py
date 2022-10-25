'''27 - Calculando la media'''

#ENTRADA

entrada = None
numeros = []


while entrada != 0:
    try:
        entrada = input('Numero: ')
        entrada = float(entrada)
        numeros.append(entrada)
        if numeros[0] == 0:
            print('No hay introducido ningun valor. Vuelva a intentarlo.')
            entrada = None
            numeros = []
    except:
        entrada = None
    

#PROCESO

numeros.pop()

calculo_media = sum(numeros) / len(numeros)


#SALIDA

print(numeros)
print('La media es: {:.2f}'.format(calculo_media))