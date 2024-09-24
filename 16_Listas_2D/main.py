"""
listas 2D: tambien conocidas como listas multidimensionales, basicamente es una lista dentro de otra lista separada
por una coma.
"""

bebidas = ["cafe", "soda", "te"]
cena = ["pizza", "hamburguesa", "hot dog"]
postres = ["pastel", "helado"]

comida = [bebidas, cena, postres]

print(comida)
# Salida: [['cafe', 'soda', 'te'], ['pizza', 'hamburguesa', 'hot dog'], ['pastel', 'helado']]

print(comida[0])
# Salida: ['cafe', 'soda', 'te']

print(comida[0][0])
# Salida: cafe

