# Corte de cadenas: se utiliza para crear una subcadena, extrayendo elementos de otra cadena

# Para dividir una cadena podemos usar el operador de indexacion: '[indice de inicio:indice de finalizacion:un paso]'
"""
NOTA:
indice de inicio: empieza a contar desde 0
indice de finalizacion: empieza a contar desde 1
paso: es un campo opcional, es la cantidad en que estamos incrementando nuestro indice entre el inicio
y la finalizacion
"""

# Ejemplo 1: extraemos la primera letra del nombre
nombre = "Alex Smith"
primerNombre = nombre[0]
print(primerNombre)
# Salida: A

# Ejemplo 2: Cortamos los primeros 4 caracteres de mi cadena 
nombre = "Alex Smith"
primerNombre = nombre[0:4]
print(primerNombre)
# Salida: Alex

# Forma abreviada: Si dejamos el primer indice en blanco, python asumira que es 0
nombre = "Alex Smith"
primerNombre = nombre[:4]
print(primerNombre)
# Salida: Alex 

# Ejemplo 3: Cortamos el apellido
nombre = "Alex Smith"
primerNombre = nombre[:4]
apellido =  nombre[5:10]
print(apellido)
# Salida: Smith

# Forma abreviada: Si dejamos el ultimo indice en blanco, python asumira que es el final de tu cadena
nombre = "Alex Smith"
primerNombre = nombre[:4]
apellido =  nombre[5:]
print(apellido)
# Salida: Smith

# Ejemplo 4: Extraer de nombre cada segundo caracter, incluido el primero
nombre = "Alex Smith"
primerNombre = nombre[:4]
apellido =  nombre[5:]
nombre2 = nombre[0:10:2]
print(nombre2)
# Salida: Ae mt

# Ejemplo 5: Usamos el objeto slice()
# slice(indice de inicio, indice de finalizacion, un paso): objeto para cortar cadenas
webSite = "http://www.google.com"
# Creamos el objeto
slice = slice(11, -4)
print(webSite[slice])
# Salida: google




