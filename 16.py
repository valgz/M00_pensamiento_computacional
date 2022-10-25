#ENTRADA

alcohol_real_acumulado = 0

mas_bebidas = True

while mas_bebidas == True:

    num_bebidas = int(input('Numero de bebidas: \t \t'))
    volumen_cc = float(input('Volumen en cm3 de la bebida: \t'))
    grado_al = float(input('Grado alcohólico: \t \t'))

    alcohol_real_acumulado += num_bebidas * ((volumen_cc * grado_al * 0.8) / 100)

    agregar_bebida = input('¿Quieres agregar otra bebida? (S/N): ').upper()
    if agregar_bebida == 'S':
        mas_bebidas = True
    elif agregar_bebida == 'N':
        mas_bebidas = False

horas = float(input('Horas transcurridas: \t \t'))

#PROCESO

CONVERSOR_UBES = 0.1

ubes_totales = alcohol_real_acumulado * CONVERSOR_UBES 

alcoholemia_inmediata = ubes_totales * 0.3

alcoholemia_real = round(alcoholemia_inmediata - 0.15 * horas, 3)

#SALIDA
if alcoholemia_real <= 0:
    print(f'Su nivel de alcohol en sangre es nulo.\nUsted puede conducir')
elif alcoholemia_real > 0 and alcoholemia_real <= 0.5:
    print(f'Alcohol en sangre: {alcoholemia_real}\nEl máximo permitido es: 0.5 g/l\nUsted puede conducir')
else:
    print(f'Alcohol en sangre: {alcoholemia_real}\nEl máximo permitido es: 0.5 g/l\nUsted no puede conducir')









