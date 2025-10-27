"""
Funciones VOID, no devuelven nada solo hacen algo.
"""

def mostrar():
    print ("hola usuario! \n ")


def cuadradoDeN(n):
    return n**2

numeroUsu= int (input("Introduce un numero \n"))
resultado= cuadradoDeN(numeroUsu)

print (f"Hola! el cuadrado de {numeroUsu} es: {resultado}")
