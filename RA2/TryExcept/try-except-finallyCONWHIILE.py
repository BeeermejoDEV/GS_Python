"""
Try except finally con WHILE:
"""

while(True):
    try:
        n1= int (input("Escribe un numero: "))
        n2= int (input("Escribe un numero2: "))
        resultado=n1+n2
        print(resultado)
        break
    except:
        print("Debes introducir solo numeros. Vuelve a intentarlo: ")
    
    finally:
        print("Saliendo del sistema!")

