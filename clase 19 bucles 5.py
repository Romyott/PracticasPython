#clase 19, bucles 5
#instrucciones adicionales CONTINUE, PASS y ELSE

#continue: salta a la siguiente instruccion, ignorando la vuelta de bucle para pasar a la siguiente
#pass: devolver null en esa vuelta de bucle (como si no la hiciera); se usa mucho para definicion de clases o para maquetear
#else: simil en condicionales

for letra in "roqueford":
	if letra =="r": #evaluara el bucle a cada vuelta, si se cumple, salta esta vuelta
		continue
	print ("viendo la letra: " + letra)

#como haria si quiero contar el numero de caracteres?
nombre="Pildoras informaticas"
print(len(nombre)) #asi cuenta el espacio en blanco tambien...

contador=0 #que cuente desde cero cada letra
for i in nombre:
	if i==" ": #asi ignora el espacio en blanco
		continue
	contador+=1 #incrementa en uno al contador; equivalente a contador= contador+1
print(contador)

#usando pass, tiene usos muy especificos

#while True: #bucle infinito
#	pass #mantiene el programa ocupado hasta que se salga del mismo con Ctrl + c

class MiClase:
	pass #armar una clase nula, hasta que decida usarla

#usando else en bucles
email=input("introduce tu mail: ")
for i in email:
	if i=="@":
		arroba=True
		break; #hace que salga del bucle cuando encuentre un @
else: #es parte del for, no del if. Se ejecuta cuando termine el bucle
	arroba=False
print(arroba)

