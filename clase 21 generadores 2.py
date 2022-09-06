#clase 21, generadores 2
#nueva instruccion agregada YIELD FROM
#esto sirve para simplificar la instruccion con bucles anidados (for dentro de for, por ejemplo)

#se puede acceder al interior del elemento generado por un generador, como si fuera un array de dos dimensiones
#se accede con bucles FOR anidados.

def devuelveCiudades(*ciudades): #el * es porque va a recibir un numero indeterminado de elementos, ne este caso, tuplas
	for elemento in ciudades:
		#ahora, como podriamos acceder a cada letra que forma la ciudad?
		#for subElemento in elemento: 
		#	yield subElemento
		#o aplicar YIELD FROM:
		yield from elemento

ciudadesDevueltas=devuelveCiudades("Madrid","Barcelona","Buenos Aires","Chascomus")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas)) #cada print me va a mostrar los subelementos que forman a los elementos, o sea, cada letra dentro del nombre de cada ciudad
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

#YIELD FROM tomara cada subelemento de un elemento y me lo desglosara 
#En este ejemplo son letras del nombre de cada ciudad
#pero podrian ser numeros o listas o tuplas, etc