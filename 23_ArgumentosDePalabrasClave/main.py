"""
argumentos de palabras clave: estos son argumentos que van precedidos por un identificador
cuando los pasamos a una funcion, a diferencia de los argumentos posicionales en este caso el
orden de los argumentos no importa.
"""

def saludo(nombre, apellido, lenguaje):
    print("Hola " + nombre + " " + apellido + ", estas aprendiendo: " + lenguaje)
    
saludo(lenguaje = "Python", apellido = "Mamani", nombre = "Nestor")

# Salida: Hola Nestor Mamani, estas aprendiendo: Python