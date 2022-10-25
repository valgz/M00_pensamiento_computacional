'''SOLUCION CON LISTA'''


mas_cuentas = True
almacen = []

print('Crea un usuario y una contraseña')

#ENTRADA
while mas_cuentas == True:
    user = str(input('Usuario: '))
    password = str(input('Clave: '))
    almacen.append((user, password))
    crear_otra = str(input('¿Quieres crear otra cuenta? ').upper())
    if crear_otra == 'SI':
        mas_cuentas = True
    elif crear_otra == 'NO':
        mas_cuentas = False

#log in

print('Ingresa usuario y contraseña para entrar al sistema')

user = str(input('Usuario: '))
password = str(input('Clave: '))

user_password = (user, password)

if user_password in almacen:
    print('Entró en el sistema.')
else: 
    print('No te conozco no pasas')