#clase 35
#paquetes
#https://www.youtube.com/watch?v=nRieWujis4s&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=35

#son directorios donde se van a almacenar modulos relacionados entre si
#es una forma de organizar el codigo
#se crea formando una carpeta que contenga un archivo:
#  __init__.py

#para crear paquetes:
#1) crear una carpeta donde guardar las cosas
#2) salvar dentro un archivo __init__.py
#3) listo! asi sabe python que esa carpeta es un paquete
# 	dentro de esta carpeta guardare diferentes modulos
#	del mismo codigo final.

#para usar paquetes:
#1)debo crear un archivo desde el cual llamare al paquete
#	(no necesariamente en la misma carpeta)
#2)se llama con la instruccion: 
#FROM + nombre_paquete.nombre_modulo + IMPORT + funcion_que_quiero_llamar
#ej: from calculos.calculos_generales import dividir
#3) luego, solo darle los parametros como esta indicado en la funcion a usar

#pueden formarse subpaquetes (paquete-ception)
#igual que antes, dentro de cada carpeta tiene que estar
#el archivo __init__.py

