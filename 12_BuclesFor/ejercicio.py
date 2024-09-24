"""
Programa que simule una cuenta regresiva desde el 10 hasta el 0
"""

# Importamos el modulo time, para usar la funcion sleep()
import time

for s in range(10, 0, -1):
    print(s)
    time.sleep(1)# esperamos un segundo
    
print("Felix anio nuevo")

"""
Salida:
10
9
8
7
6
5
4
3
2
1
Felix anio nuevo
"""