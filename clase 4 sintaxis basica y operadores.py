Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 10+10
20
>>> #operador modulo, el resto de una division, se representa con %
>>> 10%3
1
>>> 26%5
1
>>> #para la potencia, se usan dos asteriscos.
>>> 5**3
125
>>> 9**3
729
>>> #para divisiones, se usa la barra. Pero esta devuelve el numero entero
>>> 9/2
4.5
>>> 9//2
4
>>> #para saber el tipo de variable, se usa el comando type()
>>> nombre = 5
>>> type(nombre)
<class 'int'>
>>> #lo reconoce como int porque en python, la variable se define por el contenido
>>> nombre2 = "Romina"
>>> type (nombre2)
<class 'str'>
>>> nombre3 = 3.14
>>> type (nombre3)
<class 'float'>
>>> #para agregar saltos de linea, se deben poner ¨ antes de cada salgo
>>> mensaje = ¨¨¨esto es
  File "<stdin>", line 1
    mensaje = ¨¨¨esto es
              ^
SyntaxError: invalid character '¨' (U+00A8)
>>> mensaje = """era con"
... estas comillas,
... boluda"""
>>> print (mensaje)
era con"
estas comillas,
boluda
>>> 