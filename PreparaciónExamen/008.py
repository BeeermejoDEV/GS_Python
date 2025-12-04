#Division segura:

while True:
    numeroUsu= int(input("Introduce un numero para ser dividido: \n"))
    divisorUsu= int(input("Introduce el divisor: \n "))

    try:
        resultado= int(numeroUsu/divisorUsu)
        resultado= float(resultado)
        print ("EL resultado es: ", resultado)
        break
    except ZeroDivisionError:
        print ("No puedes dividir entre 0!!!")
    except TypeError:
        print ("Debes introducir numeros!")
