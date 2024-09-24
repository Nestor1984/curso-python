"""
and: y (ambas condiciones deben ser verdaderas)
or: y/o (ambas condiciones pueden ser verdaderas o solo una condicion puede ser verdadera)
not(): negador
"""
temperatura = int(input("Cual es la temperatura afuera? "))

if not(temperatura >= 0 and temperatura <= 30):
    print("La temperatura esta mal hoy :(") 
elif not(temperatura < 0 or temperatura > 30):
    print("La temperatura esta bien hoy :D")   

