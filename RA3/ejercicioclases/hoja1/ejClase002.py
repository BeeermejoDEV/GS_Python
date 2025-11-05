"""
Ejercicio 7:
Reescribe el programa de calificaciones del capítulo anterior utilizando una función 
llamada computegrade, que reciba una puntuación (score) como parámetro y devuelva la 
nota (grade) como cadena de texto.
"""


def computeGrade(score):
    if (score<10 and score>0):#Aqui puse or en vez de and. mayor que 0 ,ó menor que 10 siempre son TRUE
        if (score<5):
            print ("Has sacado un insuficiente: ")
            print ((f"Su nota a sido un {score} sobre 10"))
        elif (score>=5 and score<7):
            print ("Has sacado un suficiente: ")
            print ((f"Su nota a sido un {score} sobre 10"))
        elif (score>=7 and score<9):
            print ("Has sacado un notable: ")
            print ((f"Su nota a sido un {score} sobre 10"))
        else:
            print ("Has sacado un sobresaliente: ")
            print ((f"Su nota a sido un {score} sobre 10"))

    else:
        print(f"error al introducir la nota, no puede ser menor de 0 o mayor que 10")


notaUsu=float(input ("Escriba su nota: "))
computeGrade(notaUsu)