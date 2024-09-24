
# Variables:
# +: sirve para concatenar texto (no concatena con enteros, ni con otro tipo de datos)
# type(): muestra el tipo de dato de unavariable
# str(): convierte a caracteres

# STRING
nombre = "Nestor"
apellido = "Mamani"
nombreCompleto = "Hola " + nombre + " " + apellido
print(nombreCompleto)
print(type(nombre))

# INT
edad = 19
# edad = edad + 1
edad += 1
print("Tu edad es: " + str(edad))
print(type(edad))

# FLOAT
altura = 1.77
print("Tu altura es: " + str(altura))
print(type(altura))

# BOOL
humano = False
print("Eres un humano: " + str(humano))
print(type(humano))

