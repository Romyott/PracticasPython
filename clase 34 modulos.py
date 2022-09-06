#clase 34
#modulos
#https://www.youtube.com/watch?v=t93x-vnFvP4&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=34

#que es un modulo?
#son archivos con extencion .py
#tienen su propio espacio de nombres
#pueden contener variables, funciones, clases y modulos dentro

#se usan para organizar y reutilizar codigo (digno de POO)
#se busca una mejor maniobrabilidad con respecto al codigo
#(mejor un puñado de conjuntos de lineas que un monstruo de miles de lineas)

#se crean formando un archivo de extencion .py

import clase_34_ejercicio #primero debo importar el modulo
clase_34_ejercicio.sumar(5,7) #luego lo puedo usar pero siempre que tenga en cuenta el metodo del punto
								#primero va el nombre del modulo y despues la funcion interna que quiero llamar, en este caso, suma

clase_34_ejercicio.restar(5,7)

#como hago para no escribir siempre el nombre del modulo?
#en vez de importar, escribo FROM + IMPORT

from clase_34_ejercicio import * #el * me trae todo lo de dentro del modulo, si quiero una funcion puntual, solo pongo el nombre de la misma
sumar(5,7)