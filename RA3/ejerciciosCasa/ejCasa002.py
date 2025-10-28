"""
💻 Ejercicio 8: Calculadora de descuento

Crea una función llamada calcular_descuento(precio, porcentaje)
que reciba:
el precio original de un producto

y el porcentaje de descuento (por ejemplo, 15 para un 15%)

La función debe devolver el precio final después de aplicar el descuento.
"""


def calcularDescuento(precio, descuento):
    porcentajeDesc= descuento/100
    descontado= precio*porcentajeDesc
    precioFinal= precio-descontado
    return precioFinal


precioUsu= float (input("introduzca el precio del producto \n"))
descUsu= float (input("Introduzca tambien el descuento que deseamos aplicar. \n"))
print (f"Su precio final ha sido de {calcularDescuento(precioUsu, descUsu)}")