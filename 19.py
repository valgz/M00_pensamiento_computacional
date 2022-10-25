'''IVA por paises'''

#CONSTANTES

iva_paises = {
    27 : ['Hungría'], 
    25 : ['Crocia', 'Dinamarca', 'Suecia'],
    24 : ['Finlandia', 'Rumanía'],
    23 : ['Grecia', 'Irlanda', 'Polonia', 'Portugal'],
    22 : ['Eslovenia', 'Italia'],
    21 : ['España', 'Bélgica', 'Letonia', 'Lituania', 'Países bajos', 'Republica checa'],
    20 : ['Austria', 'Bulgaria', 'Eslovaquia', 'Estonia', 'Francia', 'Reino unido'],
    19 : ['Alemania', 'Chipre'],
    18 : ['Malta'],
    15 : ['Luxemburgo']
}

#ENTRADAS

#Pedir cantidad
precio = float(input('Precio: '))
precio = round(precio, 2)

#pedir pais
pais = str(input('País: '))
pais = pais.capitalize()


#PROCESO

keys = list(iva_paises.keys())
indice_keys = 0
indice_values = 0
found = False

while not found and indice_keys < len(keys):

    values = iva_paises.get(keys[indice_keys])

    for k in values:
        if pais == values[indice_values]:
            iva = keys[indice_keys]
            found = True
            break
        else:
            indice_values += 1
            
    if not found:
        indice_values = 0
        indice_keys += 1


iva_aplicado = round((precio * iva / 100), 2)
precio_final = round((precio + iva_aplicado), 2)

#SALIDA

print(f"En el país {pais}, el IVA es de {iva}%. Sus resultados son los siguientes: \nBase:\t\t{precio}\nIVA aplicado:\t{iva_aplicado}\nTotal:\t\t{precio_final}")



#SOLUCION DRIVE
'''
ivas = {
    "hungria": 27,
    "croacia": 25,
    "dinamarca": 25,
    "suecia": 25,
    "finlandia": 24,
    "rumania": 24,
    "grecia": 23,
    "irlanda": 23,
    "polonia": 23, 
    "portugal": 23,
    "eslovenia": 22,
    "italia": 22,
    "españa": 21,
    "belgica": 21,
    "letonia": 21,
    "lituania": 21,
    "paises bajos": 21,
    "republica checa": 21,
    "austria": 20,
    "bulgaria": 20,
    "eslovaquia": 20,
    "estonia": 20,
    "francia": 20,
    "reino unido": 20,
    "alemania": 19,
    "chipre": 19,
    "malta": 18,
    "luxemburgo": 19
}

strPais = input("País de origen: ")
strPais = strPais.lower()
strPrecio = input("Precio: ")

precio = round(float(strPrecio), 2)

if ivas.get(strPais):
  iva = precio *  ivas[strPais]/100
else:
  iva = 0
  
total = precio + iva

print("Base: {:0.2f}€\nIVA: {}% - {:0.2f}€\nTotal: {:0.2f}€".format(precio, ivas[strPais], iva, total) if ivas.get(strPais) else "País no conocido")
'''