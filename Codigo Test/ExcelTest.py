
import pandas as pd #recuerda instalar modulo pandas

#cambien la ruta dependiendo de donde guarden el excel
filePath="/Users/sergiogonzalez/Documents/GitHub/ProyectoIntegradorPrimerSemestre/Archivo Exel/PInt.xlsx"
readFile=pd.read_excel(filePath)
selectCell=readFile["Preguntas"][0] #encontrar el valor especifico de una celda 

selectCell=str(selectCell.lower()) #Transforma el valor de la celda en str y la pasa a lower
res=input("escribe texto ")

res=res.lower()#pasa a lower el input

if res==selectCell: #compara la entrada con la celda
   print(True)

else:
    print(False)