
import pandas as pd #recuerda instalar modulo pandas
import time 
from os import system, name

def clear(): #Funcion para borrar contenido de terminal
    # para windows 
    if name == 'nt': 
        _ = system('cls') 
    # para mac y linux
    else: 
        _ = system('clear') 

def nombresPuntos(nuevoNombre,promedio,tot):
   #Pide Nombres de jugadores y hace suma de puntos 
   nuevoNombre.lower()
   print("")
   
   nombresjug.append(nuevoNombre)
   puntajes.append(promedio)
   
   totpn=dict(zip(nombresjug,puntajes))
   tot.append(totpn)

   nombresjug.clear()
   puntajes.clear()
   
   
#cambien la ruta dependiendo de donde guarden el excel

#filePath=
filePath="/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Archivo Exel/PInt.xlsx"

readFile=pd.read_excel(filePath)

 
tot=[]
puntajes=[]
nombresjug=[]
puntos=[]
puntosT=[]


cont=0
while cont<=5: #Si se desean agregar mas preguntas cambie el valor de comparacion

   #Asignacion de variable de celda donde estan las preguntas
   preguntacell=readFile["Preguntas"][cont] 


   #Incicsos en Excel
   resCorrectacell= readFile["Res_C"][cont]
   resIncorrectacell_1= readFile["Res_I_1"][cont]
   resIncorrectacell_2= readFile["Res_I_2"][cont]

   #Respuestas en excel
   Correctacell= readFile["Res_CC"][cont]
   Incorrectacell_1= readFile["Res_II_1"][cont]
   Incorrectacell_2= readFile["Res_II_2"][cont]

   #Da las Instrucciones al usuario
   #print("\n","Escriba el inciso que crea es es el correcto. \n Por cada pregunta correcta se suman dos puntos.")

   #Imprime la pregunta
   listaInscisos=["a","b","c"]
   contIncisos=0
   print(" ","\n",preguntacell,"\n")

   #Imprime todos los incisos de la pregunta y los acomoda
   while contIncisos<len(listaInscisos):
      for inciso in listaInscisos:
         if inciso==resCorrectacell:
            print(inciso,Correctacell,"\n",sep=" ")
            
         elif inciso==resIncorrectacell_1:
            print(inciso,Incorrectacell_1,"\n",sep=" ")
         
         elif inciso==resIncorrectacell_2:
            print(inciso,Incorrectacell_2,"\n",sep=" ")


      contIncisos=3

   cont+=1
   contIncisos+=1
   print("")



   #Condicional para saber si la respuesta esta bien 
   respuestas=True
   while respuestas==True:

      #responder preguntas y transformarlas a minusculas el input
      resUrs=input("Ingrese el inciso conrrecto: ")
      resUrs= resUrs.lower()

      if resUrs==resCorrectacell:
         puntos.append(1)
         respuestas=False
      elif resUrs==resIncorrectacell_1 or resUrs==resIncorrectacell_2:
         puntos.append(0)
         respuestas=False
      else:
         print("valor invalido")
         

for elementos in puntos:
   puntosT.append(elementos)
   promF=((sum(puntosT))*100)/len(puntosT)

time.sleep(1)
clear()

nombre=input("Ingrese su nombre: ")
nombresPuntos(nombre,promF,tot)

print(f"{nombre} usted tuvo {sum(puntosT)} de {len(puntosT)}\n por lo tanto su calif final es de {promF}")
print(tot)