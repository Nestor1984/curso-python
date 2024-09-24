"""
funcion: una funcion es un bloque de codigo que se ejecuta solo cuando se lo llama
Sintaxis:

# Declaramos la funcion
def nombreDeLaFuncion(parametros):
    # Codigo

# Invocamos a la funcion
nombreDeLaFuncion(argumentos) 
"""

# Declaramos la funcion
def saludo(primer_nombre, apellido, edad):
    print("Hola " + primer_nombre + " " + apellido)
    print("Tienes " + str(edad) + " anios")
    print("que tengas un buen dia!")

# Declaramos una variable con nuestro nombre
nombre = "Nestor"

# Invocamos a la funcion y le pasamos los argumentos
saludo(nombre, "Mamani", 20) 

"""
Salida:
Hola Nestor Mamani
Tienes 20 anios
que tengas un buen dia!
"""