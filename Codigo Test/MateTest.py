import time

def tiempo(counter):
    start = time.time()
    while True:
        time.sleep(1)
        counter = counter - 1
        print ("quedan: ",counter,"segundos")


        if (counter <= 0):
            print("Se acabó el tiempo :(")
            break

print("Preguntas de Matemáticas")
counter=int(input("Cuánto tiempo quieres? "))
tiempo(counter)
print("""pregunta 1)
7/5 + 2/3 - 1 = ?

1) 17/5   2) 8/8   3) 16/15""")
print("""pregunta 2)
Fórmula del área de un cuadrado?

1) L*L   2) 2L+L   3) 4*L""")

print("""pregunta 3)
Cuál es el valor de x?

2*x + 4 = 8

1) 4   2) 2   3) 4""")

print("""pregunta 4)
A cuánto equivale pi?


1) 3.14159   2) 3.14921   3) 3.14412""")

print("""pregunta 5)
Si un chocolate cuesta 12 pesos,
Cuántos compraré con 276 pesos?


1) 13   2) 27   3) 23""")
