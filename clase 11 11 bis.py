Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Programa de evaluacion")

nota_alumno = input() #si no abro el teclado, aca no veo nada
def evaluacion(nota_alumno):
	dato_final="aprobado"
	if nota_alumno<4:
		dato_final="desaprobado"
	return evaluacion

print(evaluacion(int(nota_alumno)))
