"""
Ejercicio 3: Adivina el número
    El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo. Después
    de cada intento, el programa indica si el número es mayor o menor. Usa try-except para
    validar que la entrada sea numérica. El juego termina cuando el usuario acierta.
"""
import random


def tabla_multiplicar(num):
    numeroUsu= int (input("Introduzca un numero: \n"))
    numeroAleatorio= random.randint(1, 100)
    print (numeroAleatorio)

    try:
            while numeroUsu!=numeroAleatorio:
                if numeroUsu>numeroAleatorio:      
                    print ("Es mas pequeño")
                    numeroUsu= int (input("Introduzca un numero: \n"))
                elif numeroUsu<numeroAleatorio:    
                    print ("Es mas grande!")
                    numeroUsu= int (input("Introduzca un numero: \n"))
            print("Enhorabuena! acertaste!")
                

    except ValueError:
        print("❌ Debes introducir un número válido.")


print("Juego adivinar el numero del 1 al 100: ")
tabla_multiplicar(0)



