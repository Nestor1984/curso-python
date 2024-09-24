"""
diccionario: es una coleccion modificable y no ordenada de pares unicos (clave: valor)
"""

# Creamos un diccionario de paises y capitales
capitales = {
    'EE.UU': 'Washington D.C',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago de Chile',
    'Brasil': 'Brasilia'
}

print(capitales['Chile']) # Imprimimos la capital de Chile
# Salida: Santiago de Chile

print()
print(capitales.get('Alemania')) # get(): verifica si un elemento existe en el diccionario
# Salida: None

print()
print(capitales.keys()) # keys(): sirve para imprimir solo las claves
# Salida: dict_keys(['EE.UU', 'Argentina', 'Chile', 'Brasil'])

print()
print(capitales.values()) # values(): sirve para imprimir solo los valores
# Salida: dict_values(['Washington D.C', 'Buenos Aires', 'Santiago de Chile', 'Brasilia'])

print()
print(capitales.items()) # items(): sirve para traer tanto las llaves como los valores
# Salida: dict_items([('EE.UU', 'Washington D.C'), ('Argentina', 'Buenos Aires'), ('Chile', 'Santiago de Chile'), ('Brasil', 'Brasilia')])

# Otra forma de mostrar todos los valores pares clave y valor de un diccionario es usar un bucle for:
# key: variable para las llaves
# value: variable para los valores
print()
for key, value in capitales.items():
    print(key, value)
"""
Salida:
EE.UU Washington D.C
Argentina Buenos Aires
Chile Santiago de Chile
Brasil Brasilia
"""

# Agregamos un valor al diccionario
print()
capitales.update({'Alemania': 'Berlin'}) # update(): sirve para agregar un valor al diccionario 
for key, value in capitales.items():
    print(key, value)
"""
Salida:
EE.UU Washington D.C
Argentina Buenos Aires
Chile Santiago de Chile
Brasil Brasilia
Alemania Berlin
"""

# Eliminamos un valor del diccionario
print()
capitales.pop('EE.UU') # pop(clave): sirve para eliminar un valor por su clave
for key, value in capitales.items():
    print(key, value)
"""
Salida:
Argentina Buenos Aires
Chile Santiago de Chile
Brasil Brasilia
Alemania Berlin
"""
    
# Limpiamos nuestro diccionario
print()
capitales.clear() # clear(): sirve para limpiar el diccionario
# Salida: 

# Podemos almacenar el tipo de dato que nosotros quisieramos dentro de nuestro diccionario
print()
capitales = {
    'EE.UU': 'Washington D.C',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago de Chile',
    'Brasil': 'Brasilia',
    'cursos': ['Python', 'C++']
}

capitales.update({'Alemania': 'Berlin'})
capitales.pop('EE.UU') 
for key, value in capitales.items():
    print(key, value)
"""
Salida:
Argentina Buenos Aires
Chile Santiago de Chile
Brasil Brasilia
cursos ['Python', 'C++']
Alemania Berlin
"""