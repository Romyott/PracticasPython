def suma():
	num1=5
	num2=7
	print(num1-num2)

suma()

def suma2(numa,numb): #con estos parametros ya definidos no hace falta que los escriba dentro de la funcion
	print(numa+numb)

suma2(7,12)
suma2(3,10)
suma2(2,3)

#y si ahora pongo variables combinadas?
def mix (num1,num2,lett1,lett2):
	print(str(num1+num2)+lett1+lett2) #debo definir en que formato las debe leer para la impresion, en este caso, todo como string

mix(1,2,"a","b")

#Funcion RETURN
def cuenta(numX, numY):
	resultado= numX + numY
	return resultado
print(cuenta(10,15)) #con esto le decimos que imprima la funcion
print(cuenta(2,5))
#parece mas complicada pero para mas adelante se puede trabajar con ese "return", no solo visualizarlo
#ej:
guardo_resultado=cuenta(5,8) #asi voy modificando la funcion conforme avance el codigo
print(guardo_resultado)

