#Guardar numero válido:

while True:
    numeroUsu= input("Introduzca un numero: ")

    try:
        numeroUsu= int (numeroUsu)
        print ("Se ha guardado correctamente: ", numeroUsu)
        break
    except ValueError:
        print("ValueError: Debes introducir un número válido")