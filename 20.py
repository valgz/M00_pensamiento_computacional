'''De numero a mes'''

number = ''

while number == '':
    try:
        number = int(input('Numero: '))
    except:
        print('Valor incorrecto. Vuelva a intentarlo')

mes = ''

if number == 1:
    mes = 'Enero'
elif number == 2:
    mes = 'Febrero'
elif number == 3:
    mes = 'Marzo'
elif number == 4:
    mes = 'Abril'
elif number == 5:
    mes = 'Mayo'
elif number == 6:
    mes = 'Junio'
elif number == 7:
    mes = 'Julio'
elif number == 8:
    mes = 'Agosto'
elif number == 9:
    mes = 'Septiembre'
elif number == 10:
    mes = 'Octubre'
elif number == 11:
    mes = 'Noviembre'
elif number == 12:
    mes = 'Diciembre'
else:
    print('Numero introducido incorrecto.')

print(mes)
