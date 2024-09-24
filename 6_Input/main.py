"""
input(): sirve para introducir cadenas de texto a traves de la consola (TODO LO QUE RECIBA SERA CADENAS DE TEXTO)
"""

nombre = input("Cual es tu nombre? ")
edad = int(input("Cuantos anios tienes? "))
altura = float(input("Que tan alto eres? "))

# edad = edad + 1

print("Hola " + nombre)
print("Tienes " + str(edad) + " anios")
print("Mides " + str(altura) + "cm")