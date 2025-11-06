"""
    Ejercicio 4: Comprobar si un número es primo
        Solicita al usuario un número entero positivo y comprueba si es primo. Usa un bucle while
        para verificar si tiene divisores y muestra el resultado. Valida la entrada con try-except.
"""

def es_primo(num):
    numeroUsu= num

    while True:
        if (numeroUsu%3 ==0 or numeroUsu%5== 0 or numeroUsu%2==0 or numeroUsu%7==0):
            print ("No es primo")
            break
        else:
            print ("Es primo")
            break


numeroUsu= int (input("escribe un numero: \n"))
es_primo(numeroUsu)