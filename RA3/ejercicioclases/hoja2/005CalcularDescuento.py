"""
Ejercicio 5: Calcular descuento
    Crea una función llamada `calcular_descuento` que reciba:
        - precio_original (float)
        - descuento (float), como argumento por palabra clave, con valor por defecto 10
    La función debe devolver el precio final tras aplicar el descuento
"""

def calcular_descuento(precio_original, descuento=10):
    return precio_original* (1- (descuento/100))

precio1= calcular_descuento(100)        ##Descuento defecto del 10%
precio2= calcular_descuento(100,20)     ##Descuento introducido

print( f" el precio1 cuesta ahora: {precio1} y el precio2 cuesta ahora: {precio2}")