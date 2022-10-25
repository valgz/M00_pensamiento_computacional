'''Tasa autonómica
Construye un programa que aplique una tasa a un precio en función de donde se aplique. 
Así si la provincia en la que se aplica es 'VA' (Valencia) se debe incrementar el precio en un 5,5%. 
En otro caso no se aplicará esta tasa. La salida debe ser distinta en función de la provincia, así:

Si el precio es 10 €
- Provincia = 'VA':
        El subtotal es 10.00€
        La tasa es 0.55€
        El total es 10.55€

- Provincia != 'VA':
        El total es 10.00€

Restricciones
Implementar este programa usando sólo un if sin usar else
Las cifras en € deben estar redondeadas al céntimo
Utiliza una sola sentencia print para dar el resultado'''



#CONSTANTE

TASA = 0.055

#ENTRADA

price = float(input('Precio: '))
province = input('Provincia: ')

#PROCESO

if province == 'VA':
    rate = price * TASA
    total = round(price + rate, 2)
    print(f"\n El subtotal es {price} €\n La tasa es {rate} €\n El total es {total} €")
if province != 'VA':
    print(f'El total es: {price} €')



#SOLUCION DRIVE

strPrecio = input("Precio...: ")
strProvincia = input("Provincia: ")

total = float(strPrecio)
strTotal = ""

if strProvincia == 'VA':
  tasa = total * 0.055
  strTotal = "El subtotal es {:.2f}€\nLa tasa es {:.2f}€\n".format(total, tasa)
  total = total + tasa

strTotal = strTotal + "El total es {:.2f}€".format(total)
print(strTotal)




