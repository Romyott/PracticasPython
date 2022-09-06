#clase 20, generadores
#estructuras de extraccion de info
#se guardan como objetos iterables (que se pueden recorrer)
#se van a almacenar de uno en uno, quedando pausado el elemento hasta que termine

#a diferencia de funciones comunes, el generador usa YIELD (no retur).
#esto hace que se construya un objeto iterable con el primer objeto creado, lo pausa y LUEGO va a ir agregando de a poco los demas
#con return (funciones comunes), nosotros vemos solo el resultado final.

#esta mecanica es util porque
	#son mas eficinetes, solo se empleara memoria cuando lo necesitemos y con menor tiempo
	#ideales para listas infinitas
	#mas ordenado ir trabajando con valores de uno en uno

#la sintaxis para generadores es DEF para definirlas y YIELD para retener el objeto

#1) como se veria con codigo tradicional:
def generaPares(limite):
	num=1
	miLista=[]
	while num<limite:
		miLista.append(num*2)
		num+=1
	return miLista
print(generaPares(10)) #aca defino limite

#2) como se veria con un generador:
def generaPares(limite):
	num=1
	while num<limite:
		yield num*2 #no necesito especificar la lista, solo le digo que, lo que guarde lo multiplique por dos
		num+=1
devuelvePares=generaPares(10) #aca genero un objeto que guarde el objeto iterable del generador

for i in devuelvePares: #a cada vuelta del generador, que me muestre lo que se guardo en el objeto iterable
	print(i) 

#3) que me imprima solo los primeros tres elementos:
print(next(devuelvePares)) #nos va a mostrar el primer valor almacenado
print("codigo largo de relleno")
print(next(devuelvePares))
#con esto veo lo util que puede ser en un codigo largo un generador

#entre llamada y llamada, el generador entra en PAUSA, ahorrando asi recursos, 
#solo generara elementos cuando lo necesite, no ocupando ese espacio en memoria

