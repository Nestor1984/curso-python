"""
ambito de una variable: es la region en la que una variable es reconocida, basicamente
una variable solo esta disponible desde dentro de la region en la que se crea.

VARIABLES LOCALES: Son variables definidas dentro de una funcion o bloque de codigo especifico y 
solo son accesibles dentro de ese bloque en el que fueron definidas.
VARIABLES GLOBALES: Son variables definidas fuera de cualquier funcion o bloque de codigo y 
pueden ser accedidas desde cualquier parte del programa.
"""

nombre = "Mamani" # VARIABLE GLOBAL

def mostrar_nombre():
    nombre = "Nestor" # VARIABLE LOCAL
    print(nombre)
    
mostrar_nombre()
print(nombre)

"""
Salida:
Nestor
Mamani
"""