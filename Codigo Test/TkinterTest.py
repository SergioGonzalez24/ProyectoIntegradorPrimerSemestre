'''
Porgrama de prueba para experimentar interfaz grafica 
modulo tkinter
'''

import tkinter

ventana=tkinter.Tk()
ventana.geometry("500x500") #define tamaño de ventana

#ETIQUETA
etiqueta= tkinter.Label(ventana,text="Hola Mundo",bg="green")#Crea una etiqueta
etiqueta.pack(side=tkinter.BOTTOM)#METODO PACK 

def saludo (nombre):
    print("HOLA " + nombre)

#BOTON
boton1=tkinter.Button(ventana,text="OK",padx=40,pady=50, command=lambda:saludo("Mundo"))
boton1.pack()

cajaTexto=tkinter.Entry(ventana)
cajaTexto.pack(side=tkinter.LEFT)


ventana.mainloop()