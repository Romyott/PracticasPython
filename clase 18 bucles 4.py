#clase 18, bucles 4
#bucle WHILE (indeterminado)
#funciona igual a un IN siempre que se cumpla la condicion, indefinidamente
#si la condicion deja de cumplirse, se sale del bucle y se sigue con el cuerpo del programa

#!!!! si no le pongo limite, puede formarse un bucle infinito, se congela el programa ahi

#while con limites
i=1
while i<=10: #con esto le doy una condicion al while
	print("Ejecucion" + str(i))
	i=i+1 #condicion contador, sino seria un bucle infinito
print("programa terminado")

#while como bucle indeterminado
edad=int(input("introduzca su edad: "))
while edad<0:
	print("edad incorrecta")
	edad=int(input("pone tu edad bien: ")) #si la edad es -, vuelve a mostrar el mensaje hasta que se ponga una edad valida
print("edad ingresada= " + str(edad))

#mas complicado? se puede combinar con condicionales

edad=int(input("deci tu edad: "))
while edad<5 or edad>100:
	print("edad invalida")
	edad=int(input("deci tu edad verdadera: "))
print("edad valida: " + str(edad))

#como salir de un bucle infinito (bucle a prueba de tontos)

import math #importo el metodo para la linea 44
numero=int(input("numero: "))
intentos=0 #va a dar un limite al while
while numero<0:
	print("no hay raiz real de numero negativo")
	if intentos == 2:
		print("demasiados intentos")
		break; #si se llega aca, se sale del bucle
	numero=int(input("numero valido: "))
	if numero<0:
		intentos=intentos+1
if intentos<2:
	solucion=math.sqrt(numero)
	print("la solucion es " + str(solucion))

