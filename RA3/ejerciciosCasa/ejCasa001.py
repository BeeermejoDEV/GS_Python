"""
Bloque 8 — Ejercicio guiado

💪 Reto: crea una función computepay(horas, tarifa)
Debe calcular el salario, considerando que las horas > 40 se pagan al 1.5x.
"""

horasUsu= int(input("Introduce cuantas horas has trabajado esta semana\n"))
tarifaUsu= int(input("Y a cuanto te pagan las horas? \n"))

print (f"Las horas que tienes son: {horasUsu} y te las pagan a {tarifaUsu} euros por hora")


def computePay(horasUsu,tarifaUsu):
    if (horasUsu>40):
        horasExtras= horasUsu-40
        pagoExtras= horasExtras*(tarifaUsu*1.5) #
        pagoNormal= 40*tarifaUsu
        salarioConExtras= pagoExtras + pagoNormal
        print (f" tu salario tiene extras: {salarioConExtras}")
    else:
        print (f"no tienes extras, tu salario es: {horasUsu*tarifaUsu}")


computePay( horasUsu, tarifaUsu)