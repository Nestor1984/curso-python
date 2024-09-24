"""
El operador ternario en Python sirve para simplificar expresiones condicionales en una sola linea. Es util para escribir codigo mas conciso y
legible cuando necesitas asignar un valor basado en una condicion. 

Sintaxis:
valor_si_verdadero if condicion else valor_si_falso
"""
edad = int(input("Por favor ingrese su edad: "))
mensaje = "Usted es mayor de edad" if edad >= 18 else "Usted es menor de edad"

print(mensaje)
"""
Salida:
Por favor ingrese su edad: 20
Usted es mayor de edad
"""