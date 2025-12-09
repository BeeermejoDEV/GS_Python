""" Escribe un programa en Python que pida al usuario un texto y clasifique sus palabras según estas reglas: 

- Palabras que empiezan por vocal. 

- Palabras que terminan en consonante. 

- Palabras que contienen algún número. 


El programa debe: 
- Separar el texto en palabras. 

- Detectar cuáles cumplen cada condición. 

- Guardarlas en un diccionario con tres listas. 

- Mostrar un informe final indicando las palabras encontradas en cada categoría y cuántas hay en cada una. """

userWord= input ("Introduzca un texto  \n")

def DivideInWords (string):
    nuevaPalabra="";
    wordsArray=[]
    for letter in string:
        if letter !=" ":
            nuevaPalabra+=letter
        elif letter ==" ":
            wordsArray.append(nuevaPalabra)
            nuevaPalabra="";
    wordsArray.append(nuevaPalabra)  #aqui estaba mi fallo. Al ser sin espacio, no guardaba la ultima palabra
    return (wordsArray)




def clasificationOfWords(array):
    listaVocal=[]
    finalConsonate=[]
    contieneNumer=[]
    for i in range(len(array)):
        if (array[i][0]).lower()== "a" or "e" or "i" or "u" or "o":
            print(listaVocal.append())




print(clasificationOfWords(DivideInWords(userWord)))