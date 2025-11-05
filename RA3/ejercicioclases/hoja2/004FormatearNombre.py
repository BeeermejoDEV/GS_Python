"""
Ejercicio 4: Formatear nombre completo
Crea una función llamada `formatear_nombre` que reciba:
    - nombre (str)
    - apellido (str)
    - orden (str), con valor por defecto "nombre_apellido" (el otro valor que podría tomar sería apellido_nombre)
La función debe devolver el nombre completo en el orden indicado
"""


def formatear_nombre(nombre, apellido, orden=1):
    if orden ==1:       return nombre +" "+ apellido 
    elif orden ==2:     return apellido +" "+ nombre
    else:               return "Error"

nombre1= formatear_nombre(nombre="David", apellido="Bermejo")               ##orden normal
nombre2= formatear_nombre(nombre="Raquel", apellido="profesora", orden=2)   ##orden inverso
print(nombre1 +" ||| "+ nombre2)
