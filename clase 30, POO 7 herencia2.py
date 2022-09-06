#clase 30, POO 7
#Herencia 2

class Vehiculos(): 

	def __init__(self, marca, modelo): 
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def	frenar(self):
		self.frena=True

	def estado(self):
		print ("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
			self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenando: ",self.frena)


class Moto(Vehiculos):
	
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el Caballito"

#SOBREESCRITURA
	def estado(self): #tomo el metodo padre y lo sobreescribo para adaptarlo a la clase hija segun necesite
		print ("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",
			self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenando: ",self.frena, "\nCaballito: ",self.hcaballito)	

miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()


class Furgoneta(Vehiculos):

	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta esta a tope"
		else:
			return "La furgoneta esta vacia"

miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class VElectricos (): #clase INDEPENDIENTE a la SUPRECLASE

	def __init__(self):
		self.autonomia=100 #km que puede recorrer

	def cargaEnergia(self):
		self.cargando=True

#HERENCIA MULTIPLE
class BiciElectrica(VElectricos,Vehiculos): #clase con HERENCIA MULTIPLE
	pass

miBici=BiciElectrica() #qué constructor hereda? El de la PRIMER clase escrita
miBici.estado() #da error porque este estado es de Vehiculos
