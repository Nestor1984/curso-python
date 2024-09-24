"""
*args: es un parametro que enpaquetara todos los argumentos en una tupla, es muy util para que una funcion
pueda aceptar una cantidad de variables de argumentos

NOTA 1: args es una abreviatura de argumentos.
NOTA 2: EL NOMBRE NO ES TAN IMPORTANTE COMO EL ASTERISCO QUE CONTIENE POR DELANTE DE EL. PODEMOS NOMBRARLA 
COMO QUERAMOS. POR EJEMPLO PODEMOS NOMBRARLA: *cosas
"""

# EJEMPLO 1:
def suma(*args): # Y lo empaquetamos en una tupla
    suma = 0
    for i in args:
        suma += i
    return suma

print(suma(1, 5, 3, 2, 7, 1)) # Pasamos todos estos argumentos 
# Salida: 19

# EJEMPLO 2:
def suma2(*args): # y lo empaquetamos en una tupla
    suma = 0
    cosas = list(args) # Convertimos nuestra tupla en una lista
    cosas[1] = 0
    for i in cosas:
        suma += i
    return suma

print(suma2(1, 5, 3, 2, 7, 1)) # Pasamos todos estos argumentos 
# Salida: 14