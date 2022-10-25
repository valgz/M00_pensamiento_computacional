#ENTRADA

numeros = []

cantidad = int(input('¿Cuantos numeros vas a introducir? '))

while len(numeros) < cantidad:
    try:
        nuevo_numero = input('Introduce un numero: ')
        nuevo_numero = float(nuevo_numero)
        if nuevo_numero in numeros:
            print(f"El valor {nuevo_numero} ya fue introducido anteriormente. Introduzca un nuevo numero.")
        else: numeros.append(nuevo_numero)
    except:
        print(f'El valor {nuevo_numero} no es valido. Vuelva a intentarlo.')


#PROCESO
print(f"El mayor es {max(numeros)}")
print(numeros)

