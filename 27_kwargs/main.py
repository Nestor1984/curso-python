"""
**kwargs: este es un parametro que empaqueta una cantidad variable de argumentos de palabra clave en un diccionario
NOTA 1: kwargs es una abreviatura de argumentos de palabras clave.
NOTA 2: EL NOMBRE NO ES TAN IMPORTANTE COMO LOS DOS ASTERISCOS QUE CONTIENE POR DELANTE DE EL. PODEMOS NOMBRARLA 
COMO QUERAMOS. POR EJEMPLO PODEMOS NOMBRARLA: **nombre
"""

def hola(**kwargs): # Y lo empaquetamos en un diccionario
    #print("Hola " + kwargs['nombre'] + " " + kwargs['apellido'] + " " + kwargs['segundo_nombre'])
    print("Hola", end=" ") # end=" ": Decimos que en lugar de agregar un salto de linea al final del mensaje, agregue un espacio en blanco.
    # Imprimimos los valores del diccionario
    for clave, valor in kwargs.items():
        print(valor, end=" ") # end=" ": Decimos que en lugar de agregar un salto de linea al final del mensaje, agregue un espacio en blanco.
    
hola(titulo="Senor", nombre="Nestor", apellido="Mamani", segundo_nombre="Python") # Pasamos todos estos argumentos, con sus claves

# Salida: Hola Senor Nestor Mamani Python 