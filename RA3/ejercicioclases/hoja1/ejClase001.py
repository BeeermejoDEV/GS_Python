"""
Ejercicio 6:
Reescribe tu programa de cálculo de pago con el tiempo extra (hora y media) 
y crea una función llamada computepay, la cual reciba dos parámetros (horas y tarifa).
"""

def computePay(horas,tarifa):
    if (horas>40):
        horasExtras= horas-40
        salario = (horasExtras*(tarifa*1.5))+((horas-horasExtras)*tarifa)
        print (f"Tu salario es de: {salario}")
    else:
        salario = horas*tarifa
        print (f"tu salario es de: {salario}")

horasUsu= float (input("Escriba cuantas horas trabaja por favor: \n"))
tarifaUsu= float (input("Escribe a cuanto te pagan la hora porfavor: \n"))

computePay(horasUsu, tarifaUsu)