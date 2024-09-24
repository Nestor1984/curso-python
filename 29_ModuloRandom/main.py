"""
Modulo random: es una biblioteca estandar que proporciona funciones para generar numeros aleatorios
"""

import random # Importamos la biblioteca random

# Ejemplo:
# randint(valorMinimo, valorMaximo): Genera un numero entero aleatorio dentro de un rango (incluye ambos extremos del rango)
# random(): Genera un numero flotante aleatorio entre 0.0 y 1.0 (incluye: 0.0, pero no incluye 1.0)
# choice(): Selecciona un elemento al azar de una secuencia (Puede ser una lista, tupla, cadena, etc)
# shuffle(): Mezcla aleatoriamente los elementos de una lista (La lista original es modificada directamente)
x = random.randint(1, 6)
y = random.random()
print(x)
print(y)
"""
Salida:
4
0.7095518169333124
"""

mi_lista = ['Piedra', 'Papel', 'Tijera']
z = random.choice(mi_lista)
print(z)
# Salida: Papel

cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
random.shuffle(cartas)
print(cartas)
# Salida: ['5', '7', 'K', '1', '2', 'A', 'Q', 'J', '8', '9', '6', '3', '4']