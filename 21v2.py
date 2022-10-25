#ENTRADA

numeros = []

while len(numeros) < 10:
    try:
        nuevo_numero = input('Introduce un numero: ')
        nuevo_numero = int(nuevo_numero)
        if nuevo_numero in numeros:
            print(f"El valor {nuevo_numero} ya fue introducido anteriormente. Introduzca un nuevo numero.")
        numeros.append(nuevo_numero)
    except:
        print(f'El valor {nuevo_numero} no es valido. Vuelva a intentarlo.')


#PROCESO
print(f"El mayor es {max(numeros)}")

