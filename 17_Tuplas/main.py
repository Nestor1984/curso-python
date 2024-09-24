"""
tuplas: las tuplas son colecciones ordenadas e inmutables, muy similares a las listas
pero estan ordenadas y no pueden modificarse (son muy utiles para agrupar datos relacionados)
"""

# Metodos para tuplas:
# count(valor): nos dice cuantas veces aparece un valor en la tupla
estudiantes = ('Alex', 22, 'M', 'Anto', 22, 'F')
print(estudiantes.count('Alex'))
print(estudiantes.count(22))
"""
Salida:
1
2
"""

# index(valor): nos permite encontrar el indice de un valor especifico
print()
estudiantes = ('Alex', 22, 'M', 'Anto', 22, 'F')
print(estudiantes.index('M'))
"""
Salida:
2
"""

# Mostramos el contenido de una tupla usando el bucle for
print()
estudiantes = ('Alex', 22, 'M')
for x in estudiantes:
    print(x)
"""
Salida:
Alex
22
M
"""

# Verificamos si un valor especifico existe en la tupla
print()
estudiantes = ('Alex', 22, 'M')
if 'Alex' in estudiantes:
    print("Alex esta aqui")
"""
Salida:
Alex esta aqui
"""
