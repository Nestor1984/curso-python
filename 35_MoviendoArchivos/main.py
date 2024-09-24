"""
Moviendo archivos:

os: proporciona una forma de interactuar con el sistema operativo.
"""
import os

origen = 'test.txt'
destino = 'C:\\Users\\Usuario\\Desktop\\test.txt' # NOTA: Se debe colocar doble '\' para que python reconozca la ruta

try:
    if os.path.exists(destino): # Si ya existe un archivo en la ruta especificada por 'destino'
        print('Ya hay un archivo en este destino!')
    else: # Si no hay un archivo en el destino
        os.replace(origen, destino) # Esta funcion mueve el archivo de origen a destino
        print(origen + ' fue movido')
except FileNotFoundError: # FileNotFoundError: es una excepcion que ocurre cuando se intenta acceder a un archivo o directorio que no existe
    print(origen + ' no fue encontrado!')
