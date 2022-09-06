#condicionales
#IF emplea una serie de operadores de comparacion que son <> (mayor y menor que), 
#== (igual), <= >= (menor/mayor o igual que) y != (diferente que)

def evaluacion(nota):
	valoracion="aprobado" #estado por defaul que va a evaluarse con el if
	if nota<5: 
		valoracion="desaprobado" #despues del if siempre debe haber sangria, siempre que sea parte del condicional
	return valoracion

print(evaluacion(4)) #pasa por el if
print(evaluacion(6)) #no pasa por el if porque no cumple la condicion

#que pasa si quiero introducir la nota por teclado?
#se emplea la funcion input(), esta espera a que introduscamos datos por teclado, sino no avanza
print("Programa de evaluacion")

nota_alumno = input("introduce nota: ") #si no abro el teclado, aca no veo nada
def evaluacion(nota_alumno):
	valoracion="aprobado"
	if nota_alumno<4:
		valoracion="desaprobado"
	return valoracion

print(evaluacion(int(nota_alumno))) #DEBO especificar que la salida es un numero (int) sino da error





