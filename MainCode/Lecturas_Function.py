'''
Descripcion de Programa:

Desarrollado por:
@

'''

from os import system, name
import time

#Funcion Principal, posteriormente importada en main 
def Lecturas ():

    #Funcion para borrar contenido de terminal
    def clear(): 
        # para windows 
        if name == 'nt': 
            _ = system('cls') 
        # para mac y linux
        else: 
            _ = system('clear') 

    #Lectura y ejercicos 1
    def lectura1 ():  
        '''Esta funcion llama la primer lectura y sus preguntas'''
        #Rutas; colocar ruta nueva en caso de ser necesario y maracar como comentario las que no estan en uso

        #german=("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Lecturas/El_Congreso_de_los_ratones.txt")
        sergio=("/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/Lecturas/El_Congreso_de_los_ratones.txt")

        print("")
        lectura=open(sergio,"r") #Cambiar ruta dependiendo el usuario

        print("LECTURA 1:\n")
        time.sleep(1)
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

        #Rutas; colocar ruta nueva en caso de ser necesario y maracar como comentario las que no estan en uso

        #german=("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Lecturas/Preguntas1.txt")
        sergio=("/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/PreguntasLecturas/Preguntas1.txt")

        print("")
        preguntas=open(sergio,"r") #Cambiar ruta dependiendo el usuario

        print("PREGUNTAS 1\n")
        time.sleep(1)
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
            prompt2=input('Introduzca "ok" para continuar\n')
            prompt2.lower()
            if prompt2=="ok":
                valid2=True
                clear()
            else:
                print ('Entrada no valida')
        

    #Lectura y ejercicos 2 
    def lectura2 (): 
        '''Esta funcion llama la segunda lectura y sus preguntas correspondientes'''

        #Rutas; colocar ruta nueva en caso de ser necesario y maracar como comentario las que no estan en uso

        #german=("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Lecturas/El_raton_campesino_y_el_rico_cortesano.txt")
        sergio=("/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/Lecturas/El_raton_campesino_y_el_rico_cortesano.txt")

        lectura=open(sergio,"r") #Cambiar ruta dependiendo el usuario

        print("LECTURA 2:\n")
        time.sleep(1)        
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

        #Rutas; colocar ruta nueva en caso de ser necesario y maracar como comentario las que no estan en uso

        #german=("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Lecturas/Preguntas2.txt")
        sergio=("/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/PreguntasLecturas/Preguntas2.txt")


        preguntas=open(sergio,"r") #Cambiar ruta dependiendo el usuario

        print("PREGUNTAS 2\n")
        time.sleep(1)
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

    #Ejecutar ejercicios de lectura 1 y 2
    lectura1()
    lectura2()



#Test independiente de Lecturas
'''
try:
    Lecturas()
except FileNotFoundError:
    print("Cambiar de path")
    print("No se encontro el archivo")
'''
