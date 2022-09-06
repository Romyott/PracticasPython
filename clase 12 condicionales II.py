#clase 12 condicionales II 
# en esta clase, explicacion de else y elif
#puede haber if solos pero else siempre tiene que tener UN if asociado

print("verificacion de acceso")

edad_usuario = int(input("Pone tu edad en numero: "))
if edad_usuario<18:
	print("raja de aca, pendejx")
else: #else va identado a la misma altura del if que le corresponde
	print("dale, pasa pibx")
print("fin del programa")

#Que pasa si necesito poner mas de una condicion?
#ahi se usa elif

print("verificacion de edad")

edad_usuario = int(input("Deci tu edad: "))
if edad_usuario<18:
	print("raja pibx")
elif edad_usuario>=110: #hay que ponerle la condicion que deberia cumplir tambien
	print("ke so vampiro vo?")
else:
	print("dale, pasa pasa")

#otro ejemplo con mas datos
#puedo poner casi tantos elif como necesite

nota_alumno=int(input("introduce la nota: "))
if nota_alumno<5:
	print("Insuficiente")
elif nota_alumno<6:
	print("Suficiente")
elif nota_alumno<7:
	print("Bien")
elif nota_alumno<9:
	print("Notable")
else:
	print("Sobresaliente")

