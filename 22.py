"""
Solucionando problemas del coche
"""

partida = input('¿Arranca? (s/n) ')
partida.lower()

if partida == 's':
    clic = input('¿Suena un click-click? ')
    if clic == 's':
        print('Reemplaza la batería.')
    else:
        enciende = input('¿Se enciende el coche pero no arranca? ')
        if enciende == 's':
            print('Revisa las bujías')
        else:
            cala = input('¿Arranca el coche y luego se cala? ')
            if cala == 's':
                inyeccion = input('¿Tiene el coche inyección de combustible? ')
                if inyeccion == 's':
                    print('Lleva el coche al taller. ')
                else:
                    print('Abre y cierra el starter. ')
else:
    bornes = input('¿Estan los bornes de la bateria corroídos? ')
    if bornes == 's':
        print('Limpia los bornes y vuelve a arrancar.')
    else: 
        print('Reemplaza los cables y arranca de nuevo. ')

    

