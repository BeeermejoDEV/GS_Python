#Vamos a definir una cadena y la vamos a pasar a minúsculas, eliminar los espacios
# y las letras pares las vamos a cambiar por asteriscos


palabra = input ("Introduzca una cadena porfavor!")

def convertToLowerCase(string):
    palabraMinusculas= string.lower()
    return palabraMinusculas


def withOutSpaces(string):
    return string.replace(" ", "")

def PairLettersAddItem(string):
    counter=0
    nuevaPalabra="";
    for letter in string:
        counter+=1
        if counter%2==0:
            nuevaPalabra+="*"
        else:
            nuevaPalabra+=letter
    return nuevaPalabra



def completeExercise(string):
    return PairLettersAddItem(withOutSpaces(convertToLowerCase(string)))

print(completeExercise(palabra))
