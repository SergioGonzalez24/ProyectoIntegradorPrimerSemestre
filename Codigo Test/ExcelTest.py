
import pandas as pd #recuerda instalar modulo pandas


#cambien la ruta dependiendo de donde guarden el excel
filePath="/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Archivo Exel/PInt.xlsx"
readFile=pd.read_excel(filePath)
 
cont=0

while cont<=5:
   #celda de preguntas
   preguntacell=readFile["Preguntas"][cont] 


   #Incicsos en Excel
   resCorrectacell= readFile["Res_C"][cont]
   resIncorrectacell_1= readFile["Res_I_1"][cont]
   resIncorrectacell_2= readFile["Res_I_2"][cont]

   #Respuestas en excel
   Correctacell= readFile["Res_CC"][cont]
   Incorrectacell_1= readFile["Res_II_1"][cont]
   Incorrectacell_2= readFile["Res_II_2"][cont]


   listaInscisos=["a)","b)","c)"]
   contIncisos=0

   print("","\n",preguntacell)
   while contIncisos<len(listaInscisos):
      for inciso in listaInscisos:
         if inciso==resCorrectacell:
            print(inciso,Correctacell,sep="")
         elif inciso==resIncorrectacell_1:
            print(inciso,Incorrectacell_1,sep="")
         elif inciso==resIncorrectacell_2:
            print(inciso,Incorrectacell_2,sep="")
      contIncisos=3
   

   cont+=1
   contIncisos+=1
