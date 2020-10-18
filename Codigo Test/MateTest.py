import time

def tiempot(tlim, time_0):
    tnow = time.perf_counter()
    return (tnow - time_0 > tlim)        
    
    
def pregunta(nump, pregunt, opciones, correcta, cambiot=5):
    print("pregunta " + str(nump) + ")")    
    print(pregunt)    
    print(opciones)
    respuesta = int(input("respuesta: "))
    print("")
    if (respuesta==correcta):
        print("¡Respuesta Correcta! +5 segundos.")
        return cambiot
    else:
        print("¡Respuesta incorrecta! -5 segundos.")
        return -cambiot
        

def quiz_mate():
    tlim = int(input("Cuánto tiempo quieres? "))
    print("Límite de tiempo: {}".format(tlim))
    time_0 = time.perf_counter()
    
    # manera larga:
    tinc = pregunta(1, "7/5 + 2/3 - 1 = ?", 
                                 "1) 17/5   2) 8/8   3) 16/15",3,)
    
    tlim = tlim + tinc # esta es la parte larga
    
    tinc = pregunta(2, "Fórmula del área de un cuadrado?", 
                                 "1) L*L   2) 2L+L   3) 4*L",1,)
    tlim = tlim + tinc
    
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
    
    if (tiempot(tlim, time_0)):
        print('Se acabó el tiempo!')
        return
    
    print('¡Bien hecho!')
    print("Te sobraron:",round(elapsed,2), "segundos")
quiz_mate()
