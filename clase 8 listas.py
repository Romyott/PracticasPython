#las listas permiten guardar diferentes tipos de datos (simil array en otros lenguajes)
#y tambien pueden agreandarse conforme necesite

#sus marcas distintivas con los corchetes []

lista_perritos = ["Galletito","Lola","Pepo"]
print(lista_perritos) #el primer elemento de una lista es el CERO, no el UNO.

#lista mixta
lista_mix=["Tomas", 5, 3.14, "Romina", "Australia", "Nueva Zelanda", True]
print(lista_mix)

#visualizacion
print(lista_perritos[2]) #asi llamo a un elemento particular
print(lista_perritos[0]) #recordar que la lista comienza en CERO
print(lista_perritos[-2])#los indices negativos, los cuenta de atras para adelante, pero ahi si cuenta desde UNO, no desde CERO
print(lista_perritos[1:2])#PORCION DE LISTA, me muestra desde el numero que le diga primero(uno), hasta el anterior al ultimo numero(llame hasta el 2, me muestra el 1)
print(lista_perritos[:2])#asi le pido que me muestre los dos primeros
print(lista_perritos[2:])#asi le pido que imprima desde el 2 hasta el final de la lista (solo tengo 3 jaja)

#agregar elementos
lista_perritos.append("Rosita") #append agrega de a UN ELEMENTO, al final de la lista
print(lista_perritos)
lista_perritos.insert(2,"Tito") #insert permite insertar un elemento EN EL LUGAR DONDE LE DIGAMOS
print(lista_perritos)
lista_perritos.extend(["Tigra","NoTengoMasPerritos"]) #con extend, agrego otra lista al final de mi lista original
print(lista_perritos)

#eliminar elementos
lista_perritos.remove("NoTengoMasPerritos") #elimina un elemento que yo diga
print(lista_perritos)
lista_perritos.pop() #elimina EL ULTIMO elemento de una lista
print(lista_perritos)

#dame el indice
print(lista_perritos.index("Rosita")) #aca le pido que me diga en que indice esta el elemento Rosita
print(lista_perritos.index("Galletito"))

#multiples objetos repetidos
lista_perritos.append("Rosita") #que pasa si tengo varios elementos con igual valor?
print(lista_perritos)
print(lista_perritos.index("Rosita")) #me muestra el indice del PRIMER ELEMENTO EN APARECER

#decime si hay tal cosa
print("Rosita" in lista_perritos) #da TRUE, significa que hay al menos una Rosita en lista
print("Tomas" in lista_perritos) #da FALSE porque no hay un Tomas en lista

#unir listas
lista_sumada = lista_perritos + lista_mix #+ funcionan como concatenador
print(lista_sumada)

#repetir listas
lista_repetida = lista_mix*3 #el * funciona como multiplicador
print(lista_repetida)