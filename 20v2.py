number = int(input('Numero: '))
language = int(input('Idioma. (0=Español) (1=Ingles): '))

numbers_months = {
    1 : ['Enero', 'January'], 
    2 : ['Febrero', 'February'],
    3 : ['Marzo', 'March'], 
    4 : ['Abril', 'April'], 
    5 : ['Mayo', 'May'], 
    6 : ['Junio', 'June'],
    7 : ['Julio', 'July'], 
    8 : ['Agosto', 'August'], 
    9 : ['Septiembre', 'September'], 
    10 : ['Octubre', 'October'], 
    11 : ['Noviembre', 'November'], 
    12 : ['Diciembre', 'December']
}

posicion = numbers_months.get(number)

if language == 0:
    mes = posicion[0]
elif language == 1:
    mes = posicion[1]

print(mes)
