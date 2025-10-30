"""
n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce otro numero: "))


resultado = n1+n2
print(resultado)

#dara error si el usuario no da numeros:
"""

#como solucionarlo con try-except



"""
    Por lo que, funciona de la siguiente forma:
        try:
            intenta hacer esto, y si da error al realizar esto:
        except:
            salta este error.

        y luego esta el finally: 
            se ejecuta si o si.
"""

try:
        n3= int(input("Escribe un numero: "))
        n4= int(input("Escribe otro numero"))

        resultado2= n3+n4
        print(resultado2)

except:
        print("error2. Has introducido algo que no es un numero: ")
    
finally:
        print("Se imprime si o si")