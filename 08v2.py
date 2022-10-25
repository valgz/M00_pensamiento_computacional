#ENTRADA

num_personas = ''

while num_personas == '':
    try:
        num_personas = input('¿Cuantas personas hay? ')
        num_personas = int(num_personas)
        if num_personas <= 0:
            print('El valor', num_personas, 'no es valido. Intentelo de nuevo')
            num_personas = ''
    except:
        print('El valor', num_personas, 'no es valido. Intentelo de nuevo')
        num_persona = ''

num_pizzas = ''

while num_pizzas == '':
    try:
        num_pizzas = input('¿Cuantas pizzas hay? ')
        num_pizzas = int(num_pizzas)
        if num_pizzas <= 0:
            print('El valor', num_pizzas, 'no es valido. Intentelo de nuevo')
            num_pizzas = ''
    except:
        print('El valor', num_pizzas, 'no es valido. Intentelo de nuevo')
        num_pizzas = ''

#CALCULOS

total_porciones = num_personas * num_pizzas

if total_porciones % 2 != 0:
    total_porciones += num_pizzas 

resto_porciones = total_porciones % num_personas

porciones_persona = total_porciones // num_personas

print(f'{num_pizzas} pizzas para {num_personas} personas')

if porciones_persona > 1:
    print(f"Cada persona tiene {porciones_persona} porciones.") 
else:
    print(f"Cada persona tiene {porciones_persona} porción.") 
    
if resto_porciones > 1:
    print(f"Sobran {resto_porciones} porciones.")
elif resto_porciones == 0:
    print(f"No sobra ninguna porcion")
else:
    print(f"Sobra {resto_porciones} porción.")