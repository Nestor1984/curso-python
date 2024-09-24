"""
Como leer el contenido de un archivo
"""

# Leemos el contenido del archivo test.txt linea por linea para mostrarlo en consola.
# Hacerlo de esta manera cierra los archivos automaticamente despues de abrirlo.
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError: # FileNotFoundError: Este tipo de excepción se genera cuando Python no puede encontrar el archivo especificado.
    print('El archivo no fue encontrado!')
    
""""
Salida:
Oow, puedes leer esto.
Que tengas un buen dia.
Hola me llamo Nestor Jhoel Mamani.
"""