#son similares a las listas pero con algunas restricciones
#listas pero INMUTABLES
#se pueden extraer cosas pero formando una tupla NUEVA

#para que se usan? 
#son mas rapidas que las listas, ocupan menos espacio
#formatean Strings, y pueden usarse como claves en Diccionarios (las listas no)

#las tuplas se escriben con parentesis
tupla_perritos= ("Lola","Tito","Rosita","Galletito","Tigra","Pepo") #tambien comienzan desde el CERO
print(tupla_perritos)
#tambien pueden ser mixtas
tupla_mix=("Tomas","Nueva Zelanda",3.14,100,"Romina","Australia")
print(tupla_mix)

#buscar elemento
print(tupla_perritos[2]) #elemento en posicion 2
print(tupla_perritos.index("Galletito")) #saber el index del elemento

#convertir tupla en lista
lista_perris = list(tupla_perritos) #list
print(lista_perris)

#conevertir lista en tupla
tupla_perris = tuple(lista_perris) #tuple
print(tupla_perris)

#a ver si hay algo en la tupla
print("Juan" in tupla_perritos)
print("Galletito" in tupla_perritos)

#las tuplas si permiten saber cuantos elementos repetidos pueda tener
print(tupla_mix.count(3.14)) #no tengo elementos repetidos pero bueh

#averiguar la longitud de una tupla
print(len(tupla_perritos)) #me dice el largo de la tupla
print(len(tupla_mix))

#tupla unitaria
tupa_uni= ("Wuw",) #DEBE tener la coma despues del elemento, sino no la reconoce como tupla unitaria
print(tupa_uni)
print(len(tupa_uni))

#otra forma de definir tuplas es directamente sin parentesis
tupla_directa= "Tomi", "Dublin", "finales", True
print(tupla_directa)
print(len(tupla_directa))
#no es la mejor practica porque puede confundirse cuando hay funciones con parametros a definir
#esto se llama "empaquetado de tupla"

#tambien se puede "desempaquetar", lo cual nos sirve para asignacion de valores en variables
tupla_fecha = ("Romina", 6, 11, 1989)
nombre, dia, mes, anio = tupla_fecha
print(nombre)
print(dia)
print(mes)
print(anio)
