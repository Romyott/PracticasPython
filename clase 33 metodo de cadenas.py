#clase 33
#metodo de cadenas
#https://www.youtube.com/watch?v=zH0VsRuD2ok&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=33

#las cadenas se refiere a las cadenas de palabras, los String
#los metodos son varios, simil a lo visto en SQL y otros:
#upper, lower, capitalize, count, etc...

#tener en cuenta que cada metodo puede o hasta necesita
#que se les de argumentos (lo que va entre parentesis)
#para funcionar

nombreUsuario = input("Introduce tu nombre: ")
print("El nombre es:", nombreUsuario.upper())
print("El nombre es:", nombreUsuario.lower())
print("El nombre es:", nombreUsuario.capitalize())

#y si quiero poner un numero?
#poner edad en numero, no en letra:

edad= input("introduce tu edad: ")

while(edad.isdigit()==False): #este bucle solo se cumple cuando ponga una edad numerica
	print("introduce un valor numerico")
	edad= input("introduce tu edad: ")

if (int(edad)<18):
	print("sos pendejo aun!")
else:
	print("pase pase, señor")

