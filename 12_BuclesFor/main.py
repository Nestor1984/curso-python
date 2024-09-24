# Bucles for

""" 
    1.- For in:
    Sintaxis:
    for variable in secuencia:
        Codigo a ejecutar para cada elemento en la secuencia
    
    variable: Es el nombre de la variable que tomara el valor de cada elemento de la
    secuencia en cada iteracion del bucle.
    secuencia: Es la coleccion de objetos sobre la cual se itera. Puede ser una lista,
    una tupla, un diccionario, un conjunto o una cadena.

    ------------------------------------------------------------------------------------
    
    2.- For in range:
    Sintaxis:
    for variable in range(start, stop, step):
        Codigo a ejecutar para cada numero en la secuencia
    
    start: Es el numero inicial de la secuencia. Si no se especifica, por defecto es 0.
    stop: Es el numero final de la secuencia, pero este numero no se incluye en la 
    secuencia. Es decir, range(stop) generara numeros desde 0 hasta stop - 1.
    step: Es el incremento entre cada numero en la secuencia. Si no se especifica, por
    defecto es 1.

"""

# Ejemplo 1: Imprimimos los numeros del 1 al 10
for x in range(1, 11):
    print(x)
    
"""
Salida:
1
2
3
4
5
6
7
8
9
10
"""

# Ejemplo 2: Imprimimos los numeros del 50 al 100, saltando de 2 en 2
for x in range(50, 101, 2):
    print(x)
    
"""
Salida:
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
"""

# Ejemplo 3: Imprimimos cada letra de un nombre
nombre = input("Ingresa tu nombre: ")

for x in nombre:
    print(x)
    
"""
Salida:
Ingresa tu nombre: nestor
n
e
s
t
o
r
"""

