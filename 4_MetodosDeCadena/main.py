
# len(): devuelve la longitud de una cadena
nombre = "Nestor"
print(len(nombre))
# Salida: 6

# find(): devuelve la posicion de algun caracter
nombre2 = "Nestor"
print(nombre2.find("N"))
# Salida: 0

# capitalize(): pone la primera letra de tu nombre en mayuscula
nombre3 = "nestor"
print(nombre.capitalize())
# Salida: Nestor

# upper(): convierte el texto a mayusculas
nombre4 = "nestor jhoel"
print(nombre4.upper())
# Salida: NESTOR JHOEL

# lower(): convierte el texto a minusculas
nombre5 = "NESTOR JHOEL"
print(nombre5.lower())
# Salida: nestor jhoel

# isdigit(): Verifica si nuestra cadena de texto es un digito o no
nombre6 = "Nestor Jhoel"
nombre7 = "123"
print(nombre6.isdigit())
print(nombre7.isdigit())
# Salida: False
# Salida: True

# isalpha(): Devuelve False si hay algun espacio o caracter especial
nombre8 = "Nestor_Jhoel"
print(nombre8.isalpha())
# Salida: False

# count(): Cuenta cuantos caracteres de un tipo hay en nuestra cadena
nombre9 = "Nestor Jhoel"
print(nombre9.count("e"))
# Salida: 2

# replace(caracterARemplazar, caracterPorElCualRemplazar): Nos sirve para reemplazar caracteres dentro de una cadena
nombre10 = "Nestor Jhoel"
print(nombre10.replace("e", "o"))
# Salida: Nostor Jhool

# Mostramos una cadena 4 veces
nombre11 = "Nestor"
print(nombre11*4)
# Salida: NestorNestorNestorNestor

