#clase 27, POO 4
#siguiendo el ejemplo anterior, se armara un nuevo objeto

class Coche():

	def __init__(self): #CONSTRUCTOR*
		self.largoChasis=250
		self.anchoChasis=120
		self.__ruedas=4 #ENCAPSULADO**
		self.enmarcha=False

	def arrancar(self, arrancamos): #dandole el parametro ARRANCAMOS, consigo que arrancar tambien me de el estado del coche.
		self.enmarcha=arrancamos
		if(self.enmarcha):
			return "el coche esta en marcha"
		else:
			return "el coche esta parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.anchoChasis, "y un largo de ", self.largoChasis)
		#ahora estado nos informa sobre las caracteristicas comunes de la clase
		
miCoche=Coche() 
print(miCoche.arrancar(True)) #como ARRANCAR es parametro, debo indicar si quiero que el auto arranque (TRUE) o no (FALSE)
miCoche.estado()

#ahora creamos el segundo objeto
miCoche2=Coche()
print(miCoche2.arrancar(False)) #si digo FALSE esta no-arrancado
miCoche2.estado()

#*un CONSTRUCTOR es un ESTADO INICIAL que le da estado inicial a los objetos de una clase.
#en este ejemplo, es sencillo porque hay 4 caract y dos estados nada mas.
#entre mas complejo sea, mas se emplean los CONSTRUCTORES
#su nomenclatura es super especifica __init__(self) y ponerle SELF adelante a cada estado inicial.

#**si yo no ENCAPSULO una propiedad, podria modificarla con cada objeto.
#Ej: el numero de ruedas esta declarado dentro del constructor, en la clase. Asi como esta ahora, podria modificarla desde fuera
#para evitar esto, se ENCAPSULA:
	#poner "__" antes del nombre, y listo! ya se encapsula
	# self.ruedas=4 --> self.__ruedas=4
	#!!!ojo que al llamarlo, va a haber que poner el nombre con los dos guiones.
#Tambien se pueden encapsular metodos!
