"""
Ejercicio 2: Cálculo de precio con IVA
    Crea una función llamada `calcular_precio` que reciba:
        - precio_base (float)
        - iva (float), como argumento por palabra clave, con valor por defecto 21
        La función debe devolver el precio final con el IVA aplicado.
"""

def calcularIVA(precio_base, iva):
    iva = 1+iva
    return precio_base* iva

precioIva= calcularIVA(100,iva=0.21)
print(precioIva)