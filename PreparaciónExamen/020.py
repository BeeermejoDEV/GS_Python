alumnos = ["Ana", "Luis", "Raquel"]

eleccionAlumno=0


while True:
    eleccionAlumno=input("Introduce un numero de indice: \n")
    try:
        print(alumnos[int(eleccionAlumno)])
        break
    except IndexError:
        print ("Error al introducir el índice!")
    except ValueError:
        print("Error. Debe ser un numero")
    except TypeError:
        print("Error. Debe ser un numero")