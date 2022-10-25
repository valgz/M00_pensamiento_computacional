'''Repartiendo pizza
Escribir un programa que sabiendo cuantas personas hay en una reunión y cuantas pizzas se han comprado, 
queriendo que cada persona tenga una porción de cada pizza. 
La pizza sólo puede dividirse en un número par de porciones

¿Número de personas? 7
¿Número de pizzas? 3

7 personas con 3 pizzas
Cada persona toma 3 piezas
Sobran 3 porciones'''



#ENTRADA

#pedir numero de personas
num_personas = int(input('¿Cuantas personas hay? '))
#numero de pizzas
num_pizzas = int(input('¿Cuantas pizzas hay? '))

#CALCULOS

total_porciones = num_personas * num_pizzas

if total_porciones % 2 != 0:
    total_porciones += num_pizzas 

resto_porciones = total_porciones % num_personas

porciones_persona = round(total_porciones / num_personas)

print(f'{num_personas} personas y {num_pizzas} pizzas')
print(f"Cada persona tiene {porciones_persona} porciones. Sobran {resto_porciones} porciones.")



#SOLUCION DRIVE

strPeople = input("¿Cuantas personas? ")
strPizzas = input("¿Cuantas pizzas? ")

people = int(strPeople) #7
pizzas = int(strPizzas) #3

if people % 2 == 1:
  porciones = people + 1 #8
  #ESTO SON PORCIONES POR PIZZA
else:
  porciones = people #8
  
print("{} personas toman {} pizzas".format(people, pizzas))
print("Cada persona toma {} porciones".format(pizzas))
print("Sobran {} porciones".format((porciones * pizzas) % people)) 
#Aqui el valor de people, no se modifica. Sigue siendo le valor original obtenido por input.