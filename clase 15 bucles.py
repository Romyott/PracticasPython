#clase 15, bucles
#los bucles son estructuras de ordenamiento de datos, igual que los condicionales
#repiten una o varias lineas de codigo varias veces
#sirven mucho porque permiten repetir aun sin saber cuantas veces necesito que repita
#ej: meter mal una contraseña hasta que salga bien

#existen dos tipos de bucles:
#determinado: se cuanto repite
#indeterminados: no se cuanto debera repetir, depende de las circunstancias del programa

#el bucle consta de dos partes: 
#I-declaracion del bucle (aca sabe que empieza, determina que tipo de bucle es)
#II-cuerpo del bucle (aca repite)

#bucles infinitos: entra y no sale de ahi... es del tipo II (en gral)

#FOR: for variable in elemento_a_recorrer:
#			cuerpo_bucle

for i in [3,4,5]:
	print("Hola mundo") #imprime el mensaje una vez por cada valor de la lista declarada

for i in ["Paris","Tokio","Buenos Aires"]:
	print("Wenas") #no importa que sea lo que haya dentro de la lista

for i in ["Galletito", "Lola", "Tigra"]:
	print(i) #asi le pido que imprima cada valor de la variable i, no solo que cuente por dentro

