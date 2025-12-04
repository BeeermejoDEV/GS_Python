def calificar(nota):
    try:
        if nota<5:
            print ("No has aprobado.")
        elif nota>=5 and nota<7:
            print ("Has aprobado. Tienes un suficiente")
        elif nota>=8 and nota<9:
            print (" Has aprobado. Tienes un notable")
        elif nota>=9 and nota <10:
            print ("Has aprobado. Tienes un sobresaliente")
        else:
            print ("No has introducido un numero del 1 al 10")
    except ValueError:
        print("Debes introducir numeros!")
    except TypeError:
        print ("Debes introducir numeros!")
        
notaUsu= float(input("introduce tu nota!"))

calificar(notaUsu)