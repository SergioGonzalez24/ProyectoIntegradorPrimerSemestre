from os import system, name
def clear(): 
    # para windows 
    if name == 'nt': 
        _ = system('cls') 
    # para mac y linux
    else: 
        _ = system('clear') 

def lectura1 ():
    '''Esta funcion llama la primer lectura y sus preguntas'''
    #Cambiar ruta dependiendo el usuario
    lectura=open("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Lecturas/El_Congreso_de_los_ratones.txt","r")
    print (lectura.read())
    lectura.close()

    valid1=False
    while valid1 != True:
        prompt=input('Introduzca "ok" cuando haya terminado para seguir con el ejercicio:\n')
        prompt.lower()
        if prompt=="ok":
            valid1=True
            clear()
        else:
            print ('Entrada no valida')

    contador=0
    
    #Cambiar ruta dependiendo el usuario
    preguntas=open("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Lecturas/Preguntas1.txt","r")
    print(preguntas.read())
    preguntas.close()

    pregunta1=str(input('Introduzca su respuesta a la pregunta 1:\n'))
    if pregunta1=="c":
        contador+=25
    
    pregunta2=str(input('Introduzca su respuesta a la pregunta 2:\n'))
    if pregunta2=="a":
        contador+=25

    pregunta3=str(input('Introduzca su respuesta a la pregunta 3:\n'))
    if pregunta3=="b":
        contador+=25

    pregunta4=str(input('Introduzca su respuesta a la pregunta 4:\n'))
    if pregunta4=="b":
        contador+=25

    print(f'Su puntaje para la lectura numero 1 es: {contador}/100')

    valid2=False
    while valid2 != True:
        prompt2=input('Introduzca "ok" cuando haya terminado para pasar a la siguiente lectura\n')
        prompt2.lower()
        if prompt2=="ok":
            valid2=True
            clear()
        else:
            print ('Entrada no valida')
    

def lectura2 ():
    '''Esta funcion llama la segunda lectura y sus preguntas correspondientes'''
    #Cambiar ruta dependiendo el usuario
    lectura=open("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Lecturas/El_raton_campesino_y_el_rico_cortesano.txt","r")
    print (lectura.read())
    lectura.close()

    valid1=False
    while valid1 != True:
        prompt=input('Introduzca "ok" cuando haya terminado para seguir con el ejercicio:\n')
        prompt.lower()
        if prompt=="ok":
            valid1=True
            clear()
        else:
            print ('Entrada no valida')

    contador=0

    #Cambiar ruta dependiendo el usuario
    preguntas=open("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Lecturas/Preguntas2.txt","r")
    print(preguntas.read())
    preguntas.close()

    pregunta1=str(input('Introduzca su respuesta a la pregunta 1:\n'))
    if pregunta1=="c":
        contador+=25
    
    pregunta2=str(input('Introduzca su respuesta a la pregunta 2:\n'))
    if pregunta2=="c":
        contador+=25

    pregunta3=str(input('Introduzca su respuesta a la pregunta 3:\n'))
    if pregunta3=="a":
        contador+=25

    pregunta4=str(input('Introduzca su respuesta a la pregunta 4:\n'))
    if pregunta4=="b":
        contador+=25

    print(f'Su puntaje para la lectura numero 2 es: {contador}/100')

    prompt2=input('Introduzca "fin" cuando haya terminado para terminar\n')
    prompt2.lower()
    if prompt2=="fin":
        clear()
    else:
        clear()

#Cambiar ruta dependiendo el usuario
lectura1()

lectura2()
