#--------------------------------------------------
def new_game(): # Funcion para inicializar el juego
    respuestas = []
    respuestas_correctas = 0 # Contador de respuestas correctas
    pregunta_num = 0 # Para recorrer las filas de la matriz
    
    for key in preguntas:
        print('-------------------------------------------------')
        print(key)
        for i in opciones[pregunta_num]:
            print(i)
           
        respuesta = input('Ingresa Ingresa (A, B, C o D): ').upper()
        respuestas.append(respuesta)
        
        respuestas_correctas += check_answer(preguntas.get(key), respuesta) # Pasamos el valor de las llaves en el primer argumento y en el segundo argumento pasamos la respuesta
        pregunta_num += 1
    
    display_score(respuestas_correctas, respuestas)
#--------------------------------------------------
def check_answer(respuesta_correcta, respuesta): # Funcion para verificar los datos que hemos seleccionado
    if respuesta_correcta == respuesta:
        print('CORRECTO!')
        return 1
    else:
        print('INCORRECTO!')
        return 0
#--------------------------------------------------
def display_score(respuestas_correctas, respuestas): # Funcion para calcular el puntaje que ha sacado el jugador 
    print('-------------------------------------------------')
    print('RESULTADO')
    print('-------------------------------------------------')
    
    print('Respuestas Correctas: ', end=" ")
    for i in preguntas:
        print(preguntas.get(i), end=" ") # get(i): queremos obtener los valores del diccionario preguntas
    print()
    
    print('Tus Respuestas: ', end=" ")
    for i in respuestas:
        print(i, end=" ")
    print()
    
    puntaje = int((respuestas_correctas/len(preguntas))*100)
    
    print('Puntaje: ' + str(puntaje) + '%')
#--------------------------------------------------
def paly_again(): # Funcion para preguntar al jugador si quiere jugar de nuevo
    respuesta = input('Quieres jugar de nuevo? (SI o NO): ').upper()
    
    if respuesta == 'SI':
        return True
    else:
        return False
#--------------------------------------------------

preguntas = {
    'Que idioma se habla en Brasil?: ': 'A',
    'Cual es el oceano mas grande del mundo?: ': 'B',
    'Cual es la estrella mas cercana a la tierra?: ': 'C',
    'Cual es el Segundo pais mas grande del mundo?: ': 'A'
}

opciones = [['A. Portugues', 'B. Espanol', 'C. Brasilero', 'D. Ingles'],
            ['A. Atlantico', 'B. Pacifico', 'C. Artico', 'D. Indico'],
            ['A. La Luna', 'B. Alfa Centauri A', 'C. El sol', 'D. Ninguna'],
            ['A. Canada', 'B. Rusia', 'C. EE.UU', 'D. China']]

new_game()

while paly_again():
    new_game()

print('Adios!')

"""
Salida:
-------------------------------------------------
Que idioma se habla en Brasil?: 
A. Portugues
B. Espanol
C. Brasilero
D. Ingles
Ingresa Ingresa (A, B, C o D): a
CORRECTO!
-------------------------------------------------
Cual es el oceano mas grande del mundo?:
A. Atlantico
B. Pacifico
C. Artico
D. Indico
Ingresa Ingresa (A, B, C o D): b
CORRECTO!
-------------------------------------------------
Cual es la estrella mas cercana a la tierra?:
A. La Luna
B. Alfa Centauri A
C. El sol
D. Ninguna
Ingresa Ingresa (A, B, C o D): c
CORRECTO!
-------------------------------------------------
Cual es el Segundo pais mas grande del mundo?:
A. Canada
B. Rusia
C. EE.UU
D. China
Ingresa Ingresa (A, B, C o D): a
CORRECTO!
-------------------------------------------------
RESULTADO
-------------------------------------------------
Respuestas Correctas:  A B C A
Tus Respuestas:  A B C A
Puntaje: 100%
Quieres jugar de nuevo? (SI o NO): no
Adios!
"""