from os import system, name
import pandas as pd
import time
from _ast import While


#Importar modulos de aplicaciones
from Lecturas_Function import  Lecturas
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


'''
def salir():
    while salir==True:
        regresar= int(input("Para regresar oprima 1 para salir 2"))
        clear()
        if regresar==1:
            valor=True
            return valor
            break
        elif  regresar==2:
            valor= False
            return valor
            break
        else: 
            print("valor invalido")
'''

#Funcion Principal
def main():

    print("\n Bienvenido a la apliccación Sharp Learning")
    print("\nAqui podras practicar tus habilidades de: \n\nMatematicas, Ciencias y Lectura\n")

    eleccionActividad=int(input("Seleccione el numero de las actividades a realizar: \n\n1-.Matematicas \n\n2-.Ciencias \n\n3-.Lectura \n\n4-.Salir de SharLearning "))
    salir=True

    #Empezar con programa de Matematicas
    if eleccionActividad==(1):

        clear()
        matematicas()
        Matematicas()
        #salir()

        #Salir de SharpLearning o Continuar para otra actividad
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

    #Empezar con programa de Ciencias 
    elif eleccionActividad==(2):

        clear()
        ciencias()
        Ciencias()
        #salir()

        #Salir de SharpLearning o Continuar para otra actividad
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

        

    #Empezar con Programa de Lecturas 
    elif eleccionActividad==(3):

        clear()
        #Introduccion
        print("\nLECTURA: \nA continuacion se te van a presentar diferentes lecturas.\n Lee aentamente y responde las preguntas correctamente")
        time.sleep(2)
        try:
            Lecturas() #Modulo de App lecturas

        except FileNotFoundError:
            print("No se encontro el archivo, revisar path")
            print("Para el correcto funcionamiento cambiar path dentro de Lecturas_Function.py \n")
        #salir()

        #Salir de SharpLearning o Continuar para otra actividad
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

    #Salir de SharpLearnig
    elif eleccionActividad==(4):

        clear()
        print("¿Seguro que desaea salir? \n")

        #confirmar para salir del programa
        while salir==True:
            regresar= int(input("Para cancelar oprima 1 para salir 2"))  
            clear()
            if regresar==1:
                return True
                break
            elif  regresar==2:
                return False
                break
            else: 
                print("valor invalido")

    else:
        print("\nValor no valido")
        time.sleep(0.5)
        clear()
        return True

#Main loop 
IniciarPrograma=True

while IniciarPrograma==True: #Va a repetir la funcion main hasta q el usuario quiera salir de este 
    IniciarPrograma=(main()) #reasignacion de variable dependedno lo que devuelva la funcion main

#Despedida del Programa
print("Gracias por utilizar Sharp Learning")
time.sleep(1)
clear()