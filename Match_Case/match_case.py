"""
match case: vendria a ser lo equivalente a la sentencia switch case en otros lenguajes como por ejemplo: JAVA o C++
NOTA: Esta disponible desde la version 3.10 de python
"""

color = input("Ingrese un color: ")

match color:
    
    case "verde":
        print("El color es verde")
    case "rojo":
        print("El color es rojo")
    case "azul":
        print("El color es azul")
    case _: # Opcion por default
        print("No es el color correcto")