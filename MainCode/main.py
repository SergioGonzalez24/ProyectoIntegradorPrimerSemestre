from os import system, name
import pandas as pd
import time
from _ast import While

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

def main():
    print("Bienvenido a la apliccación Sharp Learning")
    print("\nAqui podras practicar tus habilidades de: \n\nMatematicas, Ciencias y Lectura\n")

    eleccionActividad=int(input("Seleccione el numero de las actividades a realizar: \n\n1-.Matematicas \n\n2-.Ciencias \n\n3-.Lectura\n"))

    if eleccionActividad==(1):
        clear()
        matematicas()
        regresar= int(input("Para regresar oprima 1 para salir 2"))
        if regresar==1:
            return True
        elif  regresar==2:
            return False
        clear()
        
    elif eleccionActividad==(2):
        clear()
        ciencias()
        regresar= int(input("Para regresar oprima 1 para salir 2"))
        if regresar==1:
            return True
        elif  regresar==2:
            return False
        clear()

    elif eleccionActividad==(3):
        clear()
        lectura()
        regresar= int(input("Para regresar oprima 1 para salir 2"))
        if regresar==1:
            return True
        elif  regresar==2:
            return False
        clear()

    else:
        print("Valor invalido")

a=1
while a==1:
    main()
