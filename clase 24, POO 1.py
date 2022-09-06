#clase 24, POO 1
#repasar los apuntes de JAVA

#clase 25, POO 2: definiciones
#Clase: es un modelo donde se redactan las caracteristicas comunes a un grupo de objetos (ejemplo del auto: chasis y ruedas)
#Instancia/Ejemplar/Objeto de clase: son los diferentes objetos (y sus caracteristicas) que pertenecen a una clase (ejemplo: diferentes marcas de auto)
#Modularizacion: divisiones de tareas/clases que se realiza sobre el programa total, optimizar los bloques de trabajo. Cada modulo es independiente
#Encapsulacion: El funcionamiento interno de un modulo no interfiere con el funcionamiento de otro. Ademas, nadie puede verlo ni modificarlo desde fuera/otro modulo, etc.
#Metodos de acceso: conexiones entre clases para que funcionen como unidad o equipo. El acceso es parcial, debido al encapsulamiento
#Nomenclatura del punto: pseudocodigo para describir objetos, clases, sus relaciones, etc. (ej: miCoche.color="rojo"; miCoche.peso=1500; miCoche.arranca(); miCoche.frena()...)

#clase 26, POO 3:

class Coche(): #defino la clase, con Mayuscula
	largoChasis=250 #propiedad de la Clase, sera comun a todo Objeto
	anchoChasis=120
	ruedas=4
	enmarcha=False #por defecto los coches estan detenidos

#los COMPORTAMIENTOs de los objetos se definen por los METODOS asignados
	def arrancar(self): #DEFS es una funcion especial de la CLASE; DEF no es de ninguna clase
		self.enmarcha=True		#SELF refiere al OBJETO mismo de la CLASE; es el THIS de JAVA
								#escrito asi, indico que se modifique la propiedad del objeto que emplee este metodo
	def estado(self):
		if(self.enmarcha):
			return "el coche esta en marcha"
		else:
			return "el coche esta parado"							

miCoche=Coche() #OBJETO creado y CLASE asignada; INSTANCIAR una clase

print(miCoche.largoChasis) #asi veo la propiedad del objeto, traido desde la clase
print("el coche tiene",miCoche.ruedas, "ruedas")

miCoche.arrancar() #asi le indico a mi objeto que realice un comportamiento particular
print(miCoche.estado()) #con esto compruebo si arranque o no el coche (si active la linea anterior o no)

#RESUMEN:
	#Coche tiene 4 PROPIEDADES (largo, ancho, ruedas, marcha)
	#Coche tiene 2 COMPORTAMIENTOS (arrancar y estado)
