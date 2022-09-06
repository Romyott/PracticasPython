#clase 28, POO 5
#Encapsulacion, continuacion
#para que sirve? para metodos que yo quiera que sean inalterables desde fuera. 
#que solo se cumplan si ciertas condiciones se dan desde dentro de las clases, no manualmente.
#Para encapsular un METODO hay que ponerle los dos guiones bajos, como a todo lo demas

class Coche():

	def __init__(self): 
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 
		self.__enmarcha=False

	def arrancar(self, arrancamos): 
		self.__enmarcha=arrancamos
		if(self.__enmarcha):
			chequeo=self.__chequeoInterno()

		if(self.__enmarcha and chequeo):
			return "el coche esta en marcha"
		elif(self.__enmarcha and chequeo==False):
			return "algo esta mal en el chequeo"
		else:
			return "el coche esta parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, 
			"y un largo de ", self.__largoChasis)
	
	def __chequeoInterno(self): 
		print("realizando chequeo interno")
		#simulacion de chequeo interno del coche
		#solo se hara si el coche se arranca
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"	
		
		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False


miCoche=Coche() 
print(miCoche.arrancar(True)) 
miCoche.estado()

miCoche2=Coche() #como este coche no arranca, no realiza el chequeo interno
print(miCoche2.arrancar(False)) 
miCoche2.estado()

