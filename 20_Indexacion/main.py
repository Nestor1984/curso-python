"""
Indexacion
Operador de indice: representado por un conjunto de corchetes, estos brindan acceso a los
elementos de una secuencia que incluye entre otros: cadenas, listas y tuplas.
"""

# Ejemplo 1:
# islower(): devuelve verdadero cuando todos los caracteres alfabeticos que componen la cadena estan en minuscula
# capitalize(): devuelve una copia de la cadena con la primera letra en mayusculas
nombre = 'alex Smith'
if nombre[0].islower(): # Si la primera letra se encuentra en minuscula
    nombre = nombre.capitalize()
print(nombre)
# Salida: Alex smith

# Ejemplo 2:
print()
nombre = 'alex Smith'
primer_nombre = nombre[0:4] # Desde la posicion 0 cortamos 4 caracteres
print(primer_nombre)
# Salida: alex

# Ejemplo 3
# upper(): convierte a mayusculas
# lower(): convierte a minusculas
print()
nombre = 'alex Smith!'
primer_nombre = nombre[:4].upper() # Desde la posicion 0 cortamos 4 caracteres y lo convertimos a mayusculas
apellido = nombre[5:].lower() # Desde la posicion 5 cortamos hasta el ultimo caracter y lo convertimos a minusculas
ultimo_caracter = nombre[-1] # Accedemos al ultimo elemento
print(primer_nombre)
print(apellido)
print(ultimo_caracter)
""" 
Salida: 
ALEX
smith!
!
"""
