# clase 31, POO 8
# Herencia 3

# como hago si quiero usar un elemento de alguna clase padre secundaria?
# funcion SUPER()
# ejemplo:

class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad,
              "Residencia: ", self.lugar_residencia)

class Empleado(Persona):

    # agrego los datos faltantes de la clase padre
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        # le paso los datos de la clase padre, asi los reconoce
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()  # llamo a la descripcion padre
        # e incluyo los valores de esta clase
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)


Antonio = Empleado(1500, 15, "Antonio", 55, "Colombia")
Antonio.descripcion()

# existe un principio llamado "de sustitucion", en donde se emplea el "es un/a"
# un objeto de la clase, SIEMPRE sera objeto de la superclase
# asi se evitan confusiones en codigos enormes, donde se pueden perder prioridades
# en el ejemplo: un empleado ES SIEMPRE una persona
# existe un comando: ISINSTANCE(), que informa que un objeto es de una clase determinada.
print(isinstance(Antonio, Empleado))  # da TRUE si es cierto
print(isinstance(Antonio, Persona))  # tambien deberia dar TRUE


# ejemplo clase anterior (ver el final)

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Moto(Vehiculos):

    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el Caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\nCaballito: ", self.hcaballito)


miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()


class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta a tope"
        else:
            return "La furgoneta esta vacia"


miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class VElectricos ():

    def __init__(self, marca, modelo):
        self.autonomia = 100
        super().__init__(marca,modelo)
        #hay que pedirle que lo imprima

    def cargaEnergia(self):
        self.cargando = True

# HERENCIA MULTIPLE: como hago si quisiera usar elementos del constructor de
# la segunda superclase? funcion SUPER()
# SUPER(): llama al metodo de la clase padre que yo indique

class BiciElectrica(VElectricos, Vehiculos):
    pass


miBici = BiciElectrica("orbea", "1325")
