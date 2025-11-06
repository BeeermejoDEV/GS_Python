"""
Ejercicio 1: Calculadora de operaciones básicas
    Crea un programa que simule una calculadora. El usuario debe introducir dos números y
    seleccionar una operación: suma, resta, multiplicación o división. El programa debe
    repetirse hasta que el usuario decida salir. Debe manejar errores como división por cero y
    entrada de datos no numéricos.
"""

def calculadora_sencilla(numero1, numero2, operacion):
    if operacion=="sumar":
        resultado =numero1+numero2
        return resultado
    elif operacion=="restar":
        resultado= numero1-numero2
        return resultado
    elif operacion == "multiplicar":
        resultado= numero1*numero2
        return resultado
    elif operacion == "dividir":
        resultado = float (numero1/numero2)
        return resultado
    else: 
        resultado= "Error. Introduce una operacion valida: "
        return resultado

#Todas las operaciones disponibles:

operacion1= calculadora_sencilla(10,2,"sumar")
operacion2=calculadora_sencilla(10,2,"restar")
operacion3=calculadora_sencilla(10,2,"multiplicar")
operacion4= calculadora_sencilla(10,2,"dividir")
operacion5= calculadora_sencilla(10,2,"pepe")

print (operacion1)
print (operacion2)
print (operacion3)
print (operacion4)
print (operacion5)