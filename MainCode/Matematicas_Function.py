'''
Descripcion de Programa:
Este programa es de la sección de Matemáticas.
El objetivo es ayudar a que los alumnos aprendan matemáticas de una forma más entretenida,
el tiempo también les ayudará a ver cuanto tardan en cada ejercicio para así,
poder tener un registro de su progreso con la materia.
Tiene 5 problemas de matemáticas, los cuales, al responder correctamente,
suman tiempo al tiempo total, si se responden erroneamente, el tiempo diminuye.
Deberán intentar terminar el test antes de que se les acabe el tiempo.

Desarrollado por:
@Isabel Vieyra Enríquez - A01745860
'''
import time

def Matematicas ():

  def tiempot(tlim, time_0):
      tnow = time.perf_counter()
      return (tnow - time_0 > tlim)        
      
  #Función para darle el formato a las preguntas del test, ingresa número pregunta,el string de la pregunta la respuesta y la respuesta correcta    
  def pregunta(nump, pregunt, opciones, correcta, cambiot=5):

    #El cambio de tiempo por default es 5, sin embargo se puede cambiar aquí.
      print("pregunta " + str(nump) + ")")    
      print(pregunt)    
      print(opciones)


      #Si la respuesta es igual a la corracta, entonces regresa cambio de tiempo positivo.
      while True:

        respuesta = int(input("respuesta: "))
        print("")

        if (respuesta==correcta):
            print("¡Respuesta Correcta! +5 segundos.")
            False
            return cambiot

        #Si es incorrecta, el cambio de tiempo es negativo.
        elif respuesta==opciones or not(respuesta==correcta):
            print("¡Respuesta incorrecta! -5 segundos.")
            False
            return -cambiot

        else:
          print("Valor no valido")
          True
          
  #Ingresar el tiempo límite y el tiempo presente
  def quiz_mate():
      tlim = int(input("Cuánto tiempo quieres? "))
      print("Límite de tiempo: {}".format(tlim))
      time_0 = time.perf_counter()
      #incremento de tiempo (tinc) define el formato de la pregunta con la funcion pregunta
      
      # manera larga:
      tinc = pregunta(1, "7/5 + 2/3 - 1 = ?", 
                                  "1) 17/5   2) 8/8   3) 16/15",3,)
      
      tlim = tlim + tinc # esta es la parte larga
      
      tinc = pregunta(2, "Fórmula del área de un cuadrado?", 
                                  "1) L*L   2) 2L+L   3) 4*L",1,)
      tlim = tlim + tinc
      #Compara si el tiempo presente es mayor al tiempo límite, si no, entonces ya se acabó

      if (tiempot(tlim, time_0)):
          print('Se acabó el tiempo!')
          return    
      
      # manera un poco mejor
      tinc = pregunta(3, "Cuál es el valor de x?\n\n2*x + 4 = 8",
                                            "1) 4   2) 2   3) 4", 2)
      tlim = tlim + tinc
      
      # manera pro
      tinc = pregunta(4, "A cuánto equivale pi?",
                                "1) 3.14159   2) 3.14921   3) 3.14412", 1)
      tlim = tlim + tinc
      
      tinc = pregunta(5, "Si un chocolate cuesta 12 pesos,\nCuántos compraré con 276 pesos?",
                                "1) 13   2) 27   3) 23", 3)
      tlim = tlim + tinc

      elapsed=-time.perf_counter()+tlim
 
      #Se vuelve a comparar el tiempo después de las preguntas
      if (tiempot(tlim, time_0)):
          print('Se acabó el tiempo!')
          return
          #Si el usuario llega al final sin que se le acabe el tiempo, se muestra el tiempo sobrante
      #Se muestra un mensaje de bien hecho
      
      print('¡Bien hecho!')
      print("Te sobraron:",round(elapsed,2), "segundos")

  quiz_mate()    



#Test independiente de Ciencias


#Matematicas()
