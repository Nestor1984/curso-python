"""
Excepcion: Es un evento detectado durante la ejecucion que interumpe el flujo de un programa.

Apuntes:
try: Intenta ejecutar el codigo que puede fallar.
except: Maneja el error si ocurre.
as: Da un nombre al objeto de la excepcion para poder usarlo.
ZeroDivisionError: Maneja el error de dividir por cero.
ValueError: Maneja errores de valores incorrectos (como convertir una cadena no numérica a entero).
Exception: Captura cualquier otro error que no haya sido manejado específicamente.
"""

try: # Tratamos de hacer esto
    numerador = int(input("Ingresa un numero: "))
    denominador = int(input("Ingresa un numero: "))
    resultado = numerador / denominador
except ZeroDivisionError as e: # Division por cero: Si el denominador es cero, se captura el error y se imprime un mensaje.
    print(e)
    print("No puedes dividir por cero!")
except ValueError as e: # Entrada no valida: Si el usuario ingresa algo que no es un numero entero, se captura el error y se imprime un mensaje.
    print(e) 
    print("Por favor, ingresa solo numeros.")
except Exception as e: # Otros errores: Cualquier otro error no previsto se captura aqui y se imprime un mensaje.
    print(e)
    print("Algo salio Mal!")
else: # Si todo sale bien: Si no hubo errores, se imprime el resultado de la division.
    print(resultado)
finally: # Bloque 'finally': Este bloque se ejecuta siempre, haya habido errores o no, y simplemente imprime un mensaje.
    print("Esto se ejecutara siempre!")
    
"""
Salida:
Ingresa un numero: 5
Ingresa un numero: 0
division by zero
No puedes dividir por cero!
Esto se ejecutara siempre!
"""