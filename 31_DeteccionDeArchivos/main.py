"""
Vamos a verificar si existe o no una carpeta en cierta ruta
NOTA: Creamos una carpeta en el escritorio llamada 'folder'
"""
import os # Esta libreria proporciona funciones para interactuar con el sistema operativo, como manipular archivos y directorios, etc

path = 'C:\\Users\\Usuario\\Desktop\\folder' # Ruta de 'folder'

if os.path.exists(path): # Si la ubicacion existe
    print('Esa ubicacion existe!')
    if os.path.isfile(path): # Si es un archivo
        print('Es un archivo!') 
    elif os.path.isdir(path): # Si es un directorio
        print('Es un directorio!')
else:
    print('Esa ubicacion NO existe!')
    
"""
Salida:
Esa ubicacion existe!
Es un directorio!
"""


