#clase 32, POO
#polimorfismo
#https://www.youtube.com/watch?v=kV1cN_bqcSw&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=32

#sin polimorfismo:
class Coche ():
	def desplazamiento(self):
		print("Me desplazo con cuatro ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo con dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo con seis ruedas")

miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

miVehiculo3=Camion()
miVehiculo3.desplazamiento()

#con polimorfismo

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

#gracias a que el polimorfismo existe, esta funcion sabe
#a que metodo llamar aun sin haberle definido 
# ninguno en particular, solo diciendole el objeto que quiero

miCarro=Moto()
desplazamientoVehiculo(miCarro) #le paso el vehiculo del cual quiera saber el metodo
