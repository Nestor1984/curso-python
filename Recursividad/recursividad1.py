"""
La recursividad: es una tecnica donde una funcion se llama a si misma para resolver un problema mas pequeno
dentro del contexto del problema original.
"""
# 1- Sacar la suma de 1 al numero dado. Si nos dan el 5, devolvera un 5+4+3+2+1 = 15

def sumaRec(numero):
    if numero == 1:
        return 1
    else:
        return numero + sumaRec(numero-1)
    
print(sumaRec(5))
# Salida: 15