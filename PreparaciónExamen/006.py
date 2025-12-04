while True:
    numeroUsu= input ("introduce un numero: ")

    try:
        floatUsu= float(numeroUsu)
        print ("Numero válido: ", floatUsu)
        break; 
    except ValueError:
        print("Error, debes introducir un numero")