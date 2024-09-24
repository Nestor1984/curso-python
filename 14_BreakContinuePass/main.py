
# break: sirve para terminar completamente el bucle
nombre = ""

while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre != "":
        break   
"""
Salida:
Ingresa tu nombre:
Ingresa tu nombre:
Ingresa tu nombre: nestor
""" 
    
# continue: salta a la siguiente iteracion del bucle
telefono = "123-456-789"

for i in telefono:
    if i == "-":
        continue
    print(i, end="") # end="": sirve para no agregar un salto de linea
"""
Salida:
123456789
"""

# pass: no hace nada, solo actua como marcador de posicion
# NOTA: En este ejemplo no queremos imprimir el numero 13
print() # Salto de linea
for i in range(1, 21):
    if i == 13: # Si i es igual a 13
        pass # Que no haga nada
    else:
        print(i)
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
11       
12       
14       
15       
16       
17
18
19
20
"""        

