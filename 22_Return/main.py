"""
return: se utiliza dentro de las funciones para enviar valores u objetos de regreso a donde
se lo ha invocado, estos valores u objetos son conocidos como el valor de retorno de la funcion.
"""
def multiplicar(numero_uno, numero_dos):
    return numero_uno * numero_dos # Retornamos la multiplicacion

# Como nos retorna algo debemos almacenarlo en una variable, para luego imprimirlo en consola
x = multiplicar(6, 8) 
print(x)

# O tambien podemos imprimirlo directamente en consola
print(multiplicar(6, 8))

"""
Salida:
48
48
"""
