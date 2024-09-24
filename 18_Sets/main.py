"""
sets: los sets son una estructura de datos usada para almacenar elementos
de una manera similar a las listas, pero con ciertas diferencias, como por ejemplo
los elementos de un set son unicos, lo que significa que
1. NO puede haber elementos duplicados
, la segunda es que los sets son desordenados, lo que significa que
2. NO mantienen el orden de cuando son declarados
y por ultimo
3. Sus elementos deben ser inmutables
"""

# Creamos un conjunto y mostramos con un bucle for
utensilios = {"tenedor", "cuchara", "cuchillo"}
for x in utensilios:
    print(x)
"""
Salida:
cuchillo
tenedor
cuchara 
"""

# Metodos para sets:
# add(): sirve para agregar un elemento
print()
utensilios = {"tenedor", "cuchara", "cuchillo", "cuchillo", "cuchillo"}
utensilios.add("cucharita")
for x in utensilios:
    print(x)
"""
Salida:
cucharita
cuchillo
tenedor
cuchara
"""

# remove(): sirve para eliminar un elemento
print()
utensilios = {"tenedor", "cuchara", "cuchillo", "cuchillo", "cuchillo"}
utensilios.remove("cuchara")
for x in utensilios:
    print(x)
"""
Salida:
cuchillo
tenedor
"""

# pop(): sirve para eliminar un elemento al azar
print()
utensilios = {"tenedor", "cuchara", "cuchillo"}
utensilios.pop()
for x in utensilios:
    print(x)
"""
Salida:
tenedor
cuchara
"""

# clear(): sirve para eliminar todos los elementos de un conjunto
print()
utensilios = {"tenedor", "cuchara", "cuchillo"}
utensilios.clear()
for x in utensilios:
    print(x)
    
# Salida: 

# update(): sirve para unir conjuntos
print()
utensilios = {"tenedor", "cuchara", "cuchillo"}
platos = {"plato", "bol", "taza"}
utensilios.update(platos)
for x in utensilios:
    print(x)
"""
Salida:
cuchillo
tenedor
plato
cuchara
taza
bol
"""

# difference(): devuelve la diferencia del conjunto con el interable como un conjunto nuevo
print()
utensilios = {"tenedor", "cuchara", "cuchillo"}
platos = {"plato", "bol", "taza", "cuchara"}
print(utensilios.difference(platos))
# NOTA: Quita cuchara del primer conjunto por que aparece en el segundo conjunto
# Salida: {'cuchillo', 'tenedor'}

# intersection(): devuelve un elemento repetido en ambos conjuntos
print()
utensilios = {"tenedor", "cuchara", "cuchillo"}
platos = {"plato", "bol", "taza", "cuchara"}
print(utensilios.intersection(platos))
# NOTA: Nos devuelve el elemento repetido en ambos conjuntos
# Salida: {'cuchara'}

# EN RESUMEN LOS CONJUNTOS SON COLECCIONES SIN ORDEN NI INDICES Y NO PERMITEN DUPLICADOS