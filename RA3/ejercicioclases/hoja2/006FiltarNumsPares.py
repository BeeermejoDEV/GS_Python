"""
Ejercicio 7: Filtrar números pares
Crea una función llamada `filtrar_pares` que reciba una lista de números enteros 
y devuelva una nueva lista solo con los números pares.

"""

def filtrar_pares(lista=[]):
    return [n for n in lista if n%2==0]
    ## Devuelve N --> si N en LISTA si es par

numeros=[2,3,4,5,6,7,8]
pares= filtrar_pares(numeros)

print(pares)