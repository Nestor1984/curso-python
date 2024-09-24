"""
Metodo format: es un metodo disponible para las cadenas de texto

Sintaxis:
cadena_de_texto.format(valor1, valor2,...)

Donde:
cadena_de_texto: es la cadena de texto en la que quieres hacer sustituciones.
valor1, valor2, etc: son los valores que deseas usar para reemplazar los marcadores de posicion en la cadena de texto. Estos 
marcadores de posicion se indican con llaves {} dentro de la cadena de texto.

Ejemplo Simple
Un ejemplo simple de uso de format() podria ser:
nombre = "Juan"
edad = 25
print("Mi nombre es {} y tengo {} anios.".format(nombre, edad))
Este codigo imprimira: Mi nombre es Juan y tengo 25 anios.
"""

# Ejemplo 1
"""
NOTA:
{}: son marcadores de posicion
"""
str_1 = 'leche'
str_2 = 'casar'

print('Arroz con {} me quiero {}'.format('leche', 'casar'))
# Salida: Arroz con leche me quiero casar

print('Arroz con {} me quiero {}'.format(str_1, str_2))
# Salida: Arroz con leche me quiero casar

print('Arroz con {} me quiero {}'.format(str_2, str_1))
# Salida: Arroz con casar me quiero leche

print('Arroz con {1} me quiero {0}'.format(str_1, str_2))
# Salida: Arroz con casar me quiero leche

print('Arroz con {0} me quiero {1}'.format(str_1, str_2))
# Salida: Arroz con leche me quiero casar

print('Arroz con {str_2} me quiero {str_1}'.format(str_1 = 'leche', str_2 = 'casar'))
# Salida: Arroz con casar me quiero leche

print('Arroz con {str_2} me quiero {str_1}'.format(str_1 = str_1, str_2 = str_2))
# Salida: Arroz con casar me quiero leche

texto = 'Arroz con {} me quiero {}'
print(texto.format(str_1, str_2))
# Salida: Arroz con leche me quiero casar

nombre = 'Nestor'
print('Hola, mi nombre es {}'.format(nombre))
# Salida: Hola, mi nombre es Nestor

# ':10': espacio de 10 caracteres a la derecha (NOTA: Se cuenta los espacios de la cadena de texto de la variable)
print('Hola, mi nombre es {:10}. Mucho Gusto :D'.format(nombre))
# Salida: Hola, mi nombre es Nestor    . Mucho Gusto :D

# ':<10': espacio de 10 caracteres a la derecha
print('Hola, mi nombre es {:<10}. Mucho Gusto :D'.format(nombre))
# Salida: Hola, mi nombre es Nestor    . Mucho Gusto :D

# ':>10': espacio de 10 caracteres a la izquierda
print('Hola, mi nombre es {:>10}. Mucho Gusto :D'.format(nombre))
# Salida: Hola, mi nombre es     Nestor. Mucho Gusto :D

# ':^10': espacio de 5 caracteres a la izquierda y otro espacio de 5 caracteres a la derecha (PARA CENTRAR)
print('Hola, mi nombre es {:^10}. Mucho Gusto :D'.format(nombre))
# Salida: Hola, mi nombre es   Nestor  . Mucho Gusto :D

numero = 3.14159
print('El numero PI es: {}'.format(numero))
# Salida: El numero PI es: 3.14159

# ':.2f': para mostrar 2 digitos despues del punto
print('El numero PI es: {:.2f}'.format(numero))
# Salida: El numero PI es: 3.14

numero = 1000
print('El numero PI es: {:.2f}'.format(numero))
# Salida: El numero PI es: 1000.00

# ':b': para mostrar en binario
print('El numero PI es: {:b}'.format(numero))
# Salida: El numero PI es: 1111101000

# ':o': para mostrar en octal
print('El numero PI es: {:o}'.format(numero))
# Salida: El numero PI es: 1750

# ':x': para mostrar en hexadecimal
print('El numero PI es: {:x}'.format(numero))
# Salida: El numero PI es: 3e8

# ':X': para mostrar en hexadecimal, con la e en mayuscula
print('El numero PI es: {:X}'.format(numero))
# Salida: El numero PI es: 3E8

# ':e': para mostrar en notacion cientifica
print('El numero PI es: {:e}'.format(numero))
# Salida: El numero PI es: 1.000000e+03

# ':e': para mostrar en notacion cientifica, con la e en mayuscula
print('El numero PI es: {:E}'.format(numero))
# Salida: El numero PI es: 1.000000E+03