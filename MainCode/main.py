''' 
Descripcion:

Desarrollado por:
Sergio Manuel Gonzalez Vargas - A0174544 
German Guzaman Lopez - A0175
Isabel Vieyra Enríquez
'''

#modulos 

import tkinter as tk
import pandas as pd
import time 
from os import system,name

#ejercicios de secciones

def lecturas ():
    pass
def ciencia():
    pass
def matematicas():
    pass

#main

#Menu grafico de la plicación
ventana=tk.Tk()
ventana.title("Applicacion para reforzar tus estudios")
ventana.geometry("500x500")
ventana.config(bg="#0174DF")
ventana.resizable(0,0)

#Info dentro de la ventana 
textoMenu='''
Programa que ayudara a reforzar tus conocimientos de ciencias,
matematicas y lectura.
Desarrollado por: 
Sergio Gonzalez
German Guzaman 
Isabel Vieyra

'''

textoPrincipal=tk.Label(ventana,text=textoMenu,bg="#0174DF",fg="white",font="none 14 bold")
textoPrincipal.pack(side=tk.TOP)

#Boton Start
def salir_de_ventana():
    ventana.destroy()

botonS=tk.Button(ventana,text="Start",padx=40,pady=50,command=lambda:salir_de_ventana())
botonS.pack()


ventana.mainloop()







