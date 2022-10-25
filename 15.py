''' Validando contraseñas
Se trata de crear un programa que pida usuario y contraseña y que valide si coinciden. 
En el caso de que lo hagan devolver un mensaje Entró en el sistema y en el contrario No te conozco, no pasas

Lo interesante de este programa no es sólo la estructura de if necesarias, 
sino también la estructura de datos necesaria para almacenar usuarios y sus contraseñas.

-Restricciones

Utilizar if/else
Hacer el programa sensible a mayúsculas - minúsculas'''



#ENTRADA

print('Crea un usuario y una contraseña')

user = str(input('Usuario: '))
password = str(input('Clave: '))

almacen = {}
almacen.update({user: password})

#log in

print('Ingresa usuario y contraseña para entrar al sistema')

user = str(input('Usuario: '))
password = str(input('Clave: '))

user_password = (user, password)

if user_password in almacen.items():
    print('Entró en el sistema.')
else: 
    print('No te conozco no pasas')



#SOLUCION DRIVE

usuarios = (
    ("pigmonchu", "lolailo1970"),
    ("genaro23", "1234abc$"),
    ("arrumako", "killo.2018"),
)

strUser = input("User....: ")
strPwd =  input("Password: ")

ix = 0
while ix < len(usuarios) and usuarios[ix][0] != strUser:
  ix += 1
    
if ix == len(usuarios):
  print("No te conozco, no pasas")
else:
  if usuarios[ix][1] == strPwd:
    print("Entró en el sistema")
  else: 
    print("No te conozco, no pasas") # Mismo mensaje que usuario desconocido para no dar pistas a los hackers