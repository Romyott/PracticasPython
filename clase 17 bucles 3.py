#clase 17, bucles 3
#tipo RANGE en mas detalle
#notaciones especiales con PRINT

for i in range(5):
	print(f"valor de la variable = {i}") #funcion de tipo f, permite modificar los print
	#F concatena el texto con el valor de la variable en cada vuelta de bucle

#range tambien permite otras notaciones, sea adelante, atras, desde un valor dado, etc
for i in range(5,10): #le asigno un rango de valores para que cuente
	print(f"valor asignado = {i}")

for i in range(5,20,3): #asigno cada tanto debe ser el conteo
	print(i)

#otra funcion importante es LEN, que cuenta el largo de un str
print(len("Romina")) #da 6 porque son 6 letras

valido=False
email=input("ingresar email: ")
for i in range(len(email)): #le pido que de una vuelta de bucle a cada elemento del mail, evaluando si hay un @
	if email[i]=="@":
		valido=True
if valido==True:
	print("mail correcto")
else:
	print("mail incorrecto")
