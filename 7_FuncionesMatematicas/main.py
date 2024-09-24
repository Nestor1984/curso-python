# Agregamos la libreria math
import math

PI = 3.14
x = 2
y = 1
z = 3

# round(): esta funcion redondea un valor
print(round(PI))
# salida: 3

# ceil(): esta funcion redondea un numero hacia arriba al numero entero mas cercano
print(math.ceil(PI))
# salida: 4

# floor(): esta funcion redondea un numero hacia abajo
print(math.floor(PI))
# salida: 3

# abs(): retorna el valor absoluto de un numero
print(abs(-3.14))
# salida: 3.14

# pow(base, potencia): eleva un numero base a la potencia
print(pow(PI, 2))
# salida: 9.8596

# sqrt(): retorna la raiz cuadrada de un numero
print(math.sqrt(420))
# salida: 20.493901531919196

# max(): retorna el numero maximo
print(max(x, y, z))
# salida: 3

# min(): retorna el numero minimo
print(min(x, y, z))
# salida: 1