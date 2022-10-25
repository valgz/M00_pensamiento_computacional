
def arranca():
    respuesta = input('¿Arranca? (s/n) ')
    if respuesta == 's':
        return clic()
    else:
        return bornes()


def bornes():
    respuesta = input('¿Estan los bornes de la batería corroídos? ')
    if respuesta == 's':
        return 'Limpia los bornes y arranca de nuevo'
    else:
        return 'Reemplaza los cables y arranca de nuevo'


def clic():
    respuesta = input('¿Suena un clic-clic? ')
    if respuesta == 's':
        return 'Reemplaza la batería'
    else:
        return enciende()


def enciende():
    respuesta = input('¿Se enciende pero no arranca? ')
    if respuesta == 's':
        return print('Revisa la bujías. ')
    else:
        return cala()


def cala():
    respuesta = input('¿Arranca el coche y luego se cala? ')
    if respuesta == 's':
        return inyeccion()

def inyeccion():
    respuesta = input('¿Tiene el coche inyección de combustible? ')
    if respuesta == 's':
        return 'Lleva el coche al taller'
    else:
        return 'Abre y cierra el starter'

arranca()
        


