"""
listas: una lista se usa para almacenar multiples elementos dentro de una sola variable.
NOTA: En una lista siempre puedes actualizar y cambiar los elementos que se encuentran en ella
despues de declararla.
"""

# Declaramos y imprimimos la lista
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis']
print(comida)
# Salida: ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis']

# Accedemos al elemento de la posicion 4
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
print(comida[4])
# Salida: Pudding

# Cambiamos el elemento de la posicion 0
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
comida[0] = 'Helado'
print(comida[0])
# Salida: Helado

# Mostramos los elementos de la lista con un bucle for
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
comida[0] = 'Helado'
for x in comida:
    print(x)
"""
Salida:
Helado
Hamburguesa
Hot Dog
Espaguetis
Pudding
"""

# Metodos para listas:
# append(): nos permite agregar un elemento al final de la lista
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
comida[0] = 'Helado'
comida.append('Sushi')
for x in comida:
    print(x)
"""
Salida:
Helado
Hamburguesa
Hot Dog
Espaguetis
Pudding
Sushi
"""

# remove(): sirve para eliminar un valor
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
comida[0] = 'Helado'
comida.remove('Hamburguesa')
for x in comida:
    print(x)
"""
Salida:
Helado
Hot Dog
Espaguetis
Pudding
"""

# pop(): sirve para eliminar el ultimo elemento de la lista
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
comida[0] = 'Helado'
comida.pop()
for x in comida:
    print(x)
"""
Salida:
Helado
Hamburguesa
Hot Dog
Espaguetis
"""

# insert(posicion, valor): sirve para insertar un valor en una cierta posicion especifica
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
comida[0] = 'Helado'
comida.insert(0, "Pastel")
for x in comida:
    print(x)
"""
Salida:
Pastel
Helado
Hamburguesa
Hot Dog
Espaguetis
Pudding
"""

# sort(): sirve para ordenar la lista alfabeticamente
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
comida[0] = 'Helado'
comida.sort()
for x in comida:
    print(x)
    
"""
Salida:
Espaguetis
Hamburguesa
Helado
Hot Dog
Pudding
"""

# clear(): sirve para vaciar completamente la lista
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding']
comida[0] = 'Helado'
comida.clear()
for x in comida:
    print(x)
# Salida: 

# En una lista podemos almacenar distintos tipos de datos
print()
comida = ['Pizza', 'Hamburguesa', 'Hot Dog', 'Espaguetis', 'Pudding', 2, 0.5, False]
comida[0] = 'Helado'
for x in comida:
    print(x)
"""
Salida:
Helado
Hamburguesa
Hot Dog
Espaguetis
Pudding
2
0.5
False
"""