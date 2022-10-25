from mod_10 import IMPUESTO

precios = []
ejemplares = []

mas_precios = True

while mas_precios:

    precio = 'inicio'
    ejemplar = 'inicio'

    while precio != '':
        try:
            precio = float(input('Precio: '))
            precios.append(precio)
            precio = ''
        except:
            precio = 'inicio'
    
    while ejemplar != '': 
        try:
            ejemplar = int(input('Cantidad: '))
            ejemplares.append(ejemplar)
            ejemplar = ''
        except:
            ejemplar = 'inicio'
    
    continuar = input('¿Quiere introducir mas productos? (s/n) ')
    if continuar == 's':
        mas_precios = True
    else: 
        mas_precios = False

subtotal = 0

for a, b in (zip(precios, ejemplares)):
    multiplica = a * b
    subtotal += multiplica

tasa = subtotal * IMPUESTO

total = subtotal + tasa

print('Subtotal\tTasa\tTotal \n{:.2f}\t\t{:.2f}\t{:.2f}'.format(subtotal, tasa, total))




