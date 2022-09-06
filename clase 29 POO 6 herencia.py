#clase 29, POO 6
#Herencia

#es altamente util para reutilizar codigo.
#permite crear objetos similares reutilizando el codigo
#debe partirse de la base de que todos los objetos tienen caracteristicas/comportamientos en comun
#estas cosas en comun seran la CLASE PADRE o SUPERCLASE

class Vehiculos(): #SUPERCLASE
#defino las caracteristicas en comun
	def __init__(self, marca, modelo): #asi, heredaran Marca y Modelo cualquier clase hija
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
#aca defino los comportamientos en comun
	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def	frenar(self):
		self.frena=True

	def estado(self):
		print ("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
			self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenando: ",self.frena)

class Moto(Vehiculos): #primer CLASE HIJA
	pass

miMoto=Moto("Honda", "CBR") #Instancia de la clase hija
miMoto.estado()

