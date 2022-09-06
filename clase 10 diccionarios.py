#permiten almacenar de todo (datos de todo tipo, listas, tuplas, etc)
#se crea una asociacion tipo clave:valor
#los elementos no estan ordenados, es indiferente al momento de armar el diccionario

diccionario1= {"Alemania":"Berlin","Francia":"Paris","Espania":"Madrid","Australia":"Sidney"}
print(diccionario1["Francia"]) #llamo al pais para saber la capital = llamo a la CLAVE para saber el VALOR
print(diccionario1 ["Espania"])
print(diccionario1)

#agregar elementos
diccionario1["Italia"]="Lisboa" #esta mal a proposito
print(diccionario1)

#modificar un valor
diccionario1["Italia"]="Roma" #se sobreescribe el valor a cambiar
print(diccionario1)

#LOS DICCIONARIOS NO PUEDEN TENER DOS CLAVES IGUALES

#eliminar elemento
del diccionario1 ["Australia"]
print(diccionario1)

#diccionarios mixtos
dicc_mix= {"Nueva Zelanda":"Wellington", 32:"Romina", "pi":3.14, 1984:True}
print(dicc_mix)

#usar tupla para asignar las claves
tupla_dicc=["Espania","Francia","UK","Alemania"]
dicc_paises={tupla_dicc[0]:"Madrid",tupla_dicc[1]:"Paris",tupla_dicc[2]:"Londres",tupla_dicc[3]:"Berlin"}
print(dicc_paises)

#como hacer que un diccionario almacene una tupla
dicc_tuplero= {"edad":32, "nombre":"Romina", "carrera":"Biologia", "notas":[8,7,9.1,6.5,4,8]}
print(dicc_tuplero)
print(dicc_tuplero["carrera"])
print(dicc_tuplero["notas"])

#como hacer un diccionario dentro  de la tupla dentro del diccionario
dicc_tuplero2= {"edad":32, "nombre":"Romina", "carrera":"Biologia", "notas":{"promedio":[8,7,9.1,6.5,4,8]}}
print(dicc_tuplero2["notas"])

#para ver las CLAVES del diccionario
print(diccionario1.keys())
print(dicc_mix.keys())

#para ver los VALORES del diccionario
print(diccionario1.values())
print(dicc_mix.values())

#longitud del diccionario
print(len(diccionario1))
print(len(dicc_mix))