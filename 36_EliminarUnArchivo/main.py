"""
Eliminar un archivo:

remove(): sirve para eliminar (borrar) un archivo del sistema de archivos. Pertenece al modulo os.
rmdir(): sirve para eliminar (borrar) un directorio vacio del sistema de archivos. Pertenece al modulo os.
rmtree(): sirve para eliminar directorios completos con todo su contenido. Pertenece al modulo shutil.
"""

import os
import shutil

path = 'folder'

try:
    # os.remove(path) # Eliminamos un archivo
    # os.rmdir(path) # Eliminamos una carpeta vacia
    shutil.rmtree(path) # Eliminamos una carpeta con archivos
except FileNotFoundError: # FileNotFoundError: se lanza cuando se intenta acceder a un archivo o directorio que no existe en la ruta especificada.
    print('El archivo no se encontro!')
except PermissionError: #PermissionError: se lanza cuando no se tienen los permisos necesarios para realizar una operacion en un archivo o directorio.
    print('Lo siento, no tienes permiso para eliminar esta carpeta!')
except OSError: # OSError: se lanza por diversos problemas relacionados con el sistema operativo, como intentos de eliminar un directorio no vacio usando una funcion inapropiada.
    print('No puedes eliminar eso usando esa funcion!')
else:
    print(path + ' fue eliminado!')