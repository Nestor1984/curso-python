
"""
Bucle anidado: bucle dentro de otro bucle. No importa si es un bucle for o un
bucle while, el bucle interno finalizara todas sus iteraciones antes de que
termine una iteracion del bucle externo.
"""

# Ejemplo: Dibujamos el rectangulo

fila = int(input("Cuantas filas? "))
columna = int(input("Cuantas columnas? "))
simbolo = input("Ingrese su simbolo: ")

for i in range(fila): # Bucle externo: responsable de las filas
    for j in range(columna): # Bucle interno: responsable de las columnas
        print(simbolo, end="") # end="": sirve para no saltar a la siguiente linea
    print() # salto de linea
    
"""
Salida:
Cuantas filas? 5
Cuantas columnas? 6
Ingrese su simbolo: #
######
######
######
######
######
"""
