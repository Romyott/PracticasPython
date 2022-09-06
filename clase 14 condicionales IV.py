#clase 14 condicionales IV
#continuacion del anterior
#and = y si ademas
#or = o sino
#in = condicional que debe incluir

print("programa derecho a beca")
#evaluar la distancia al colegio, x>40km
#evaluar si tiene hermanos en el mismo colegio, y>2
#evaluar ingreso del hogar, z<=20000
distancia_escuela=int(input("Distancia a la escuela en km: "))
print(distancia_escuela)
numero_hermanos=int(input("Numero de hermanos inscriptos: "))
print(numero_hermanos)
salario_familiar=int(input("Saladio anual bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
	print("Posee derecho a beca")
else:
	print("No aplica a beca")

#ahora similar pero menos exigente con las condiciones
#el salario determina, o se cumplen las dos primera o prima el salario
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Posee derecho a beca")
else:
	print("No aplica a beca")

#ejemplo con in
print("elegir materia optativa")
#el alumno debe elegir una materia entre una lista de optativas
print("Materias posibles: ""Algebra ","Estadistica ","Programacion")
asignatura=input("Seleccione una materia: ")

if asignatura in ("Algebra","Estadistica","Programacion"):
	print("Materia seleccionada: " + asignatura)
else:
	print("Introduzca una materia valida")

#que pasa si escribo en mayusc cuando era minusc o al revez?
#uso las funciones lower() o upper() antes del nombre de la materia
#ejemplo: 
opcion=input("Seleccione una materia: ")
asignatura=opcion.lower()
#y con esta forma ya me libro de como sea que lo escriba la persona