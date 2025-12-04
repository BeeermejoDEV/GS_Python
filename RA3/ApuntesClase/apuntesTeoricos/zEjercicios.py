
##argumentos, variables, etc
##Ejercicio casa:   
# math.ramdom elegir ganador 


# modulo llamado calculos (areacirculo, cuadrado, triangulo) tiene esas funciones
#si no se introduce un valor necesario, el valor por defecto es 8 en todos

import math

# Si no se indica valor, será 8 por defecto

def area_circulo(radio=8):
    return round(math.pi * radio ** 2, 2)

def area_cuadrado(lado=8):
    return lado ** 2

def area_triangulo(base=8, altura=8):
    return (base * altura) / 2

