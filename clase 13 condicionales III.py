#clase 13 condicionales III
#otros codicionales como switch, and, or, in
#en python no existe la funcion switch, porque es simil el if

edad=-7
if edad<100:
	print("edad correcta")
else:
	print("edad incorrecta")
#con este ejemplo no estoy teniendo en cuenta edades negativas

edad=-7
if 0<edad<100:
	print("edad correcta")
else:
	print("edad incorrecta")
#ahora si, las edades son aquellas dentro del rango de edad que yo dije
#se pueden hacer condicionales con TODOS los operadores, es valido

print("programa evaluacion de salario")

salario_presidente=int(input("introduce monto presidente: "))
print("salario presidente: "+ str(salario_presidente)) #recordar que python es fuertemente tipado, hay que igualar todo a un tipo de dato
salario_director=int(input("introduce monto director: "))
print("salario director: "+ str(salario_director))
salario_manager=int(input("introduce monto manager: "))
print("salario manager: "+ str(salario_manager))
salario_admin=int(input("introduce monto administrativo: "))
print("salario admin: "+ str(salario_admin))

if salario_presidente>salario_director>salario_manager>salario_admin:
	print("Funciona normalmente")
else:
	print("Hay una matufia interna...")
