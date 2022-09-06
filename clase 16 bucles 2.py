#como recorrer con bucles
#el tipo RANGE
#notaciones especiales con PRINT

for i in ["Ayer", "Hoy", 15]:
	print("Hola") #imprime cada salida con un salto de linea

for i in [1,2,3]:
	print("Chau", end="") #con la finalizacion END consigo que termine la impresion sin espacios, que no salte la linea

for i in [1,2,3]:
	print("Che", end="...") #asi le digo que termine cada impresion con el valor que le ponga a las comillas

for i in "rominaott@gmail.com":
	print("Duh", end="") #va a imprimir por cada letra del mail

print("fin de encadenados")

#comprobar si es correcto o no el valor ingresado
print("prueba de mail")
email= False
for i in "rominaott@gmail.com":
	if (i=="@"): #aca le digo que se fije, si hay @ entonces es un mail valido
		email=True
if email==True:
	print("Email correcto")
else:
	print("Email incorrecto")

#!!!!por default, se asume que una variable es TRUE

#si quiero hacer el codigo anterior mas interactivo, tengo que colocarle el input
email= False
mi_email=input("introduzca su email: ")
for i in mi_email:
	if (i=="@"): #aca le digo que se fije, si hay @ entonces es un mail valido
		email=True
if email==True:
	print("Email correcto")
else:
	print("Email incorrecto")

#si quiero revisar que el mail tenga puntos:
contador= 0 #condicion inicial, contador en cero
mi_email=input("introduzca su email: ")
for i in mi_email:
	if (i=="@" or i=="."): #aca le digo que se fije, si hay @ o punto
		contador=contador+1 #siempre que cumpla una condicion u otra, que aumente la condicion en uno
if contador==2: #condicion se cumple cuando tengo @ y . (pero tambien dos @@, dos .)
	print("Email correcto")
else:
	print("Email incorrecto")

#RANGE nos permite usar un bucle FOR con contadores
for i in range(5): #forma una lista de cinco elementos, pide al bucle que repita 5 veces
	print("Hola") 

for i in range(6):
	print(i)