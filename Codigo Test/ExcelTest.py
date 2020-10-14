
import pandas as pd #recuerda instalar modulo pandas


#cambien la ruta dependiendo de donde guarden el excel
filePath="/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Archivo Exel/PInt.xlsx"

readFile=pd.read_excel(filePath)

 

ListaNombres=[]
Puntos=[]
PuntosT=[]
while True:
   cont=0
   while cont<=5:
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


      #responder preguntas y transformarlas a minusculas el input
      resUrs=input("Ingrese el inciso conrrecto: ")
      resUrs= resUrs.lower()
      puntos=0
      #Condicional para saber si la respuesta esta bien 
      if resUrs==resCorrectacell:
         Puntos.append(2)
      else:
         Puntos.append(0)

   #Pide Nombres de jugadores y hace suma de puntos 
   nuevoNombre=input("Ingrese su nombre: ")
   nuevoNombre.lower()
   
   for pos in range (len(Puntos)):
      for element in Puntos:
         if pos==2:
            print(pos,element)
   PuntosT.append(sum(Puntos))
   del Puntos[:]
   

   if not(nuevoNombre in ListaNombres):
      ListaNombres.append(nuevoNombre)

   












   