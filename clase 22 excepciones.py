#clase 22, excepciones
#es un error en tiempo de ejecucion... cuando esta todo bien pero pasa "algo inesperado"

#ejemplo: haciendo una calculadora, intento dividir por cero y cae el programa
#se cancela el flujo de ejecucion desde el error en adelante...

#se debe realizar una CAPTURA o CONTROL DE EXCEPCION
	#1) buscar la linea donde esta el error
	#2) informarle al codigo que siga ejecutando si hubiera error:
		#	try:
		#		bloque con error
		#	except NombreError:
		#		lo que quiero que el programa haga, ej: print mensaje X
		#		return algun mensaje de salida
	#LA SOLUCION SE LLAMA TRY/EXCEPT
	#3) revisar de nuevo, porque si capturo mal el error, el programa seguira cayendo 
    #4) necesito pedirle al programa que vuelva a correr la linea original? entonces
    	#podemos meter dentro del un WHILE a las lineas de codigo y que se repitan hasta que se introduzca un numero correcto
    	#ponerle in BREAK al final, para romper el bucle infinito.

#clase 23, excepciones 2
#se pueden hacer varias capturas simultaneas
#ejemplo, en un programa de calculadora, se pide que se ingresen numeros, pero si ponemos letras, cae el programa
#para evitar esto:
	#1) rodear las lineas de ingreso de numero con TRY/EXCEPT con bucle WHILE
	#2) agregar varias clausulas EXCEPT para los posibles diferentes errores que salgan
	#3) se podria agregar un EXCEPT generico, que no especifique que error ocurrio (poco recomendado, poco especifico)


#!!!!!!!!!!!!!!existe una clausula llamada FINALLY, la cual correra siempre aunque el programa tuviera error!!!!!!!!!!!!!!!!!!!
#TRY SIEMPRE TIENE QUE TERMINAR CON EXCEPT y/o FINALLY

#clase 24, excepciones 3
#se pueden generar excepciones intencionalmente
#RAISE, sirve para cuando se trabaje en POO, con clases y herencia

def evaluaEdad(edad):
	if edad<0: #creo mi tipo de error, para evitar edades invalidas 
		raise TypeError("edad inexistente") #digo YO el tipo de error que sea
				#si quisiera inventar un error, deberia definir su clase previamente, sino solo uso los que vienen en libreria
	if edad<20:
		return "sos un beibi"
	elif edad<40:
		return "hola papurro (?)"
	elif edad<65:
		return "señooooor"
	elif edad<100:
		return "todavia es joven :D"

print(evaluaEdad(18))


#calcular raices cuadradas
import math

def calculoRaiz(num1):
	if num1<0: #excepcion colocada para numeros negativos
		raise ValueError ("no puede ser negativo")
	else:
		return math.sqrt(num1)

op1= (int(input("coloca un numero: ")))	
try:
	print(calculoRaiz(op1))
except ValueError as ErrorNegativo: #redefino el error con un nombre que yo quiera ponerle
	print(ErrorNegativo) #asi es mas "limpia" la salida del error

print("finaleee")

