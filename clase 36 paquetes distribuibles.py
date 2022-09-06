#clase 36
#paquetes distribuibles
#https://www.youtube.com/watch?v=Zf9sN-w0BVE&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=36

#permite que multiples usuarios puedan usar el codigo
#sea enviandolo por mail o subiendolo a una pagina

#lo clave es CREAR e INSTALAR el paquete

#al distribuir un paquete e intalarlo tiene la ventaja de que
#no importa donde este guardado, se pueda llamarlo

#para hacerlo instalable, tengo que crear un archivo
#llamado: setup.py
#este va a tener una descripcion del paquete a instalar (autor, que hace, particularidades, etc)

# from setuptools import setup
# setup(
#		name= "paquete.calculos", <- nombre del paquete a empaquetar y distribuir
#		version="1.0",			<- en caso de querer sacar actualizaciones
#		description="Paquete matematico",
#		author="yo la mas mejor",
#		author_email="lanksfla@gmail.com"
#		url="pagina donde este alojado el paquete"
#		packages=["paquete ppal", "subpaquetes escritos con lenguaje de puntos"]
#		)

#luego puedo abrirlo desde el cmd o el powercell de Python
# en el cmd: python setup.py sdist y darle enter
#asi se crea el paquete distribuible

#queda en la carpeta madre una carpeta llamada dist con un
#archivo dentro con terminacion .tar.gz

#para instalarlo, debo dar en cmd el siguiente comando:
# pip3 install "nombre del paquete" + enter
#y listooo! 
#ahora va a funcionar desde cualquier parte del sistema operativo

#para desinstalar es: pip3 uninstall "nombre del paquete"
#y ya esta!

