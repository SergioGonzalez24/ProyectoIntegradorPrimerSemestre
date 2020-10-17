'''
Descripcion de Programa:
Esta es la sección de lectura.
El objetivo de esta función es llamar un grupo de funciones anidadas para poder evaluar el desempeño de un alumno en el área de comprensión lectora.
Está conformado por dos lecturas de poca complejidad y 4 preguntas de cada una.
Después de realizar la lectura se borra el texto para poder comprobar que el alumno haya comprendido de manera correcta lo leído e ingrese la respuesta a las preguntas.

Desarrollado por:
@Germán Guzmán López

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

        german=("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/Lecturas/El_Congreso_de_los_ratones.txt")
        #sergio=("/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/Lecturas/El_Congreso_de_los_ratones.txt")

        print("")
        lectura=open(german,"r") #Cambiar ruta dependiendo el usuario

        print("LECTURA 1:\n")
        time.sleep(1)
        print (lectura.read())
        lectura.close()

        valid1=False
        while valid1 != True:
            prompt=input('Presione la tecla ENTER para continuar con el ejercicio:\n')
            if prompt=="":
                valid1=True
                clear()
            else:
                print ('Entrada no valida')

        contador=0

        #Rutas; colocar ruta nueva en caso de ser necesario y maracar como comentario las que no estan en uso

        german=("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/PreguntasLecturas/Preguntas1.txt")
        #sergio=("/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/PreguntasLecturas/Preguntas1.txt")

        print("")
        preguntas=open(german,"r") #Cambiar ruta dependiendo el usuario

        print("PREGUNTAS 1\n")
        time.sleep(1)
        print(preguntas.read())
        preguntas.close()

        condicion1=True
        condicion2=True
        condicion3=True
        condicion4=True

        while condicion1==True:
            pregunta1=str(input('Introduzca la respuesta a la pregunta 1:\n'))
            if pregunta1=="c":
                condicion1=False
                contador+=25
            elif pregunta1=="a" or pregunta1=="b":
                condicion1=False
            else:
                print('Introduzca un inciso valido')
             
            
        while condicion2==True:
            pregunta2=str(input('Introduzca la respuesta a la pregunta 2:\n'))
            if pregunta2=="a":
                condicion2=False
                contador+=25
            elif pregunta2=="c" or pregunta2=="b":
                condicion2=False
            else:
                print('Introduzca un inciso valido')

        while condicion3==True:
            pregunta3=str(input('Introduzca la respuesta a la pregunta 3:\n'))
            if pregunta3=="b":
                condicion3=False
                contador+=25
            elif pregunta3=="a" or pregunta3=="c":
                condicion3=False
            else:
                print('Introduzca un inciso valido')
                

        while condicion4==True:
            pregunta4=str(input('Introduzca su respuesta a la pregunta 4:\n'))
            if pregunta4=="b":
                condicion4=False
                contador+=25
            elif pregunta4=="a" or pregunta4=="c":
                condicion4=False
            else:
                print('Introduzca un inciso valido')

        print(f'Su puntaje para la lectura numero 1 es: {contador}/100')

        valid2=False
        while valid2 != True:
            prompt2=input('Presione la tecla ENTER para continuar con la siguiente lectura.\n')
            if prompt2=="":
                valid2=True
                clear()
            else:
                print ('Entrada no valida')
        

    #Lectura y ejercicos 2 
    def lectura2 (): 
        '''Esta funcion llama la segunda lectura y sus preguntas correspondientes'''

        #Rutas; colocar ruta nueva en caso de ser necesario y maracar como comentario las que no estan en uso

        german=("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/Lecturas/El_raton_campesino_y_el_rico_cortesano.txt")
        #sergio=("/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/Lecturas/El_raton_campesino_y_el_rico_cortesano.txt")

        lectura=open(german,"r") #Cambiar ruta dependiendo el usuario

        print("LECTURA 2:\n")
        time.sleep(1)        
        print (lectura.read())
        lectura.close()

        valid1=False
        while valid1 != True:
            prompt=input('Presione la tecla ENTER para continuar con el ejercicio:\n')
            if prompt=="":
                valid1=True
                clear()
            else:
                print ('Entrada no valida')

        contador=0

        #Rutas; colocar ruta nueva en caso de ser necesario y maracar como comentario las que no estan en uso

        german=("/Users/germanguzman/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/PreguntasLecturas/Preguntas2.txt")
        #sergio=("/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/MainCode/PreguntasLecturas/Preguntas2.txt")


        preguntas=open(german,"r") #Cambiar ruta dependiendo el usuario

        print("PREGUNTAS 2\n")
        time.sleep(1)
        print(preguntas.read())
        preguntas.close()

        condicion1=True
        condicion2=True
        condicion3=True
        condicion4=True

        while condicion1==True:
            pregunta1=str(input('Introduzca la respuesta a la pregunta 1:\n'))
            if pregunta1=="c":
                condicion1=False
                contador+=25
            elif pregunta1=="a" or pregunta1=="b":
                condicion1=False
            else:
                print('Introduzca un inciso valido')
             
            
        while condicion2==True:
            pregunta2=str(input('Introduzca la respuesta a la pregunta 2:\n'))
            if pregunta2=="c":
                condicion2=False
                contador+=25
            elif pregunta2=="a" or pregunta2=="b":
                condicion2=False
            else:
                print('Introduzca un inciso valido')

        while condicion3==True:
            pregunta3=str(input('Introduzca la respuesta a la pregunta 3:\n'))
            if pregunta3=="a":
                condicion3=False
                contador+=25
            elif pregunta3=="b" or pregunta3=="c":
                condicion3=False
            else:
                print('Introduzca un inciso valido')
                

        while condicion4==True:
            pregunta4=str(input('Introduzca la respuesta a la pregunta 4:\n'))
            if pregunta4=="b":
                condicion4=False
                contador+=25
            elif pregunta4=="a" or pregunta4=="c":
                condicion4=False
            else:
                print('Introduzca un inciso válido')


        print(f'Su puntaje para la lectura numero 2 es: {contador}/100')

        prompt2=input('Presione la tecla ENTER para terminar.\n')
        if prompt2=="":
            clear()
        else:
            clear()

    #Ejecutar ejercicios de lectura 1 y 2
    lectura1()
    lectura2()



#Test independiente de Lecturas

try:
    Lecturas()
except FileNotFoundError:
    print("Cambiar de path")
    print("No se encontro el archivo")
