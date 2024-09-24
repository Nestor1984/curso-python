"""
Escribir un archivo en python:

with: Simplifica el codigo al eliminar la necesidad de cerrar manualmente el recurso, ya que Python se encarga de eso automaticamente al finalizar el bloque with.
open(nombre_archivo, modo[, encoding]): se utiliza para abrir archivos en diferentes modos de acceso, como lectura, escritura o ambos.
nombre_archivo: Es el nombre o la ruta del archivo que quieres abrir.
modo: Especifica el modo en el que deseas abrir el archivo. Algunos de los modos comunes son:
'r': Lectura (default). Abre el archivo para leer. (VIENE POR DEFECTO)
'w': Escritura. Abre el archivo para escribir. Si el archivo ya existe, se truncara (se eliminará su contenido anterior).
'a': Anadir. Abre el archivo para escribir al final del mismo, conservando el contenido actual.
'b': Modo binario. Abre el archivo en modo binario (por ejemplo, 'rb' para leer en modo binario).
encoding (opcional): Especifica la codificación de caracteres que se usará al leer o escribir en el archivo. Por ejemplo, 'utf-8', 'latin-1', etc.
"""
texto = '\nWoww'

with open('test.txt', 'a') as file:
    file.write(texto) # Escribimos en el archivo