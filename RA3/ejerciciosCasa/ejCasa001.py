"""
Bloque 8 — Ejercicio guiado

💪 Reto: crea una función computepay(horas, tarifa)
Debe calcular el salario, considerando que las horas > 40 se pagan al 1.5x.
"""

horasUsu= int(input("Introduce cuantas horas has trabajado esta semana\n"))
tarifaUsu= int(input("Y a cuanto te pagan las horas? \n"))

print (f"Las horas que tienes son: {horasUsu} y te las pagan a {tarifaUsu} euros por hora")


def computePay(horasUsu,tarifaUsu):
    if (horasUsu>40):#si pasa las 40 horas: 

        horasExtras= horasUsu-40 #aqui calculamos los extras que recibe a *1.5
        pagoExtras= horasExtras*(tarifaUsu*1.5) #error con la coma... muy tonta pero era lo que daba error
        pagoNormal= 40*tarifaUsu #aqui calculamos lo que recibe el usuario sin extras
        salarioConExtras= pagoExtras + pagoNormal #calculo del salario de extras + salario normal
        print (f" tu salario tiene extras: {salarioConExtras}") #imprime resultado


    else: #en caso de no pasar de 40 horas:
        print (f"no tienes extras, tu salario es: {horasUsu*tarifaUsu}") #devuelve su salario sin sus extras


computePay( horasUsu, tarifaUsu)