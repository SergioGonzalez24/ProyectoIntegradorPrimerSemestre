from os import system, name
import pandas as pd
import time
from _ast import While

#Importar modulos de aplicaciones
from Lecturas_Function import Lecturas
from Matematicas_Function import Matematicas
from Ciencias_Function import Ciencias


def clear(): #Funcion para borrar contenido de terminal
    # para windows 
    if name == 'nt': 
        _ = system('cls') 
    # para mac y linux
    else: 
        _ = system('clear') 

def matematicas():
    pass

def ciencias():
    pass

def lectura():
    pass


def main(): #Funcion Principal 
    print("Bienvenido a la apliccación Sharp Learning")
    print("\nAqui podras practicar tus habilidades de: \n\nMatematicas, Ciencias y Lectura\n")

    eleccionActividad=int(input("Seleccione el numero de las actividades a realizar: \n\n1-.Matematicas \n\n2-.Ciencias \n\n3-.Lectura\n"))
    salir=True

    if eleccionActividad==(1):

        clear()
        matematicas()
        Matematicas()
        
        while salir==True:
            regresar= int(input("Para regresar oprima 1 para salir 2"))
            clear()
            if regresar==1:
                return True
                break
            elif  regresar==2:
                return False
                break
            else: 
                print("valor invalido")

        clear()

    
    elif eleccionActividad==(2):

        clear()
        ciencias()
        Ciencias()

        while salir==True:
            regresar= int(input("Para regresar oprima 1 para salir 2"))
            clear()
            if regresar==1:
                return True
                break
            elif  regresar==2:
                return False
                break
            else: 
                print("valor invalido")

        

    elif eleccionActividad==(3):

        clear()
        lectura()
        Lecturas()

        while salir==True:
            regresar= int(input("Para regresar oprima 1 para salir 2"))
            clear()
            if regresar==1:
                return True
                break
            elif  regresar==2:
                return False
                break
            else: 
                print("valor invalido")

        

#Main loop 
IniciarPrograma=True

while IniciarPrograma==True: #Va a repetir la funcion main hasta q el usuario quiera salir de este 
    IniciarPrograma=(main()) #reasignacion de variable dependedno lo que devuelva la funcion main

#Salida del programa 
print("Gracias por utilizar Sharp Learning")
time.sleep(1)
clear()