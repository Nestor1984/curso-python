"""
Copiando Archivos:

shutil: es un modulo que proporciona varias funciones para realizar operaciones de archivos y colecciones de archivos.
copyfile('origen', 'destino'): Copia el contenido de un archivo a otro archivo.
copy('origen', 'destino'): Copia el contenido de un archivo y sus permisos a un nuevo archivo.
copy2('origen', 'destino'): Copia el contenido de un archivo y toda su metainformación (permisos, fechas de creación y modificación, etc.) a un nuevo archivo.
"""
import shutil

shutil.copyfile('test.txt', 'copy.txt') # NOTA: El archivo del segundo argumento no existe, asi que lo creara.

