# modulos: un modulo es archivo que contiene codigo python en donde dentro de este archivo puede contener funciones, clases, etc.

"""
FORMA 1:
Sintaxis:
import nombreDelModulo
"""
import mensaje

mensaje.hola()
mensaje.adios()
print()
"""
Salida:
Hola, que tengas un buen dia!
Adios, que tengas un tiempo maravilloso!
"""

"""
FORMA 2:
Sintaxis:
as: para poner alias
import nombreDelModulo as alias
"""
import mensaje as msg

msg.hola()
msg.adios()
print()
"""
Salida:
Hola, que tengas un buen dia!
Adios, que tengas un tiempo maravilloso!
"""

"""
FORMA 3:
Sintaxis:
from: de
from nombreDelModulo import metodo1, metodo2
"""
from mensaje import hola, adios

hola()
adios()
print()
"""
Salida:
Hola, que tengas un buen dia!
Adios, que tengas un tiempo maravilloso!
"""

"""
FORMA 4:
Sintaxis:
*: significa todo
from nombreDelModulo import *
"""
from mensaje import *

hola()
adios()
"""
Salida:
Hola, que tengas un buen dia!
Adios, que tengas un tiempo maravilloso!
"""