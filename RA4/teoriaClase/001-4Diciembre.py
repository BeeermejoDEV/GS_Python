#Clase 4 diciembre.
#Clase que hay que crear un ejercicio de cadenas. El cual, buscamos aprender y que se pueda resolver a traves de la API

##Enunciado:
#Crear una funcion que cuente el numero de letras que tiene un string, el numero de numeros y el numero de espacios.
#La funcion debe devolver un string con el siguiente formato:
#"tienes X letras, Y numeros y Z espacios"


nombreDeAlumno = input("Introduce tu nombre porfavor y tu edad: ");

def contadorSoloDeLetras (string):
    contador=0;
    contadorNumero=0;
    contadorEspacios=0;
    numero=[]
    edad ="";
    for letra in string:
        if (letra.isdigit()==True):
            contadorNumero+=1
            numero.append(letra)
        elif (letra.isalpha()):
            contador+=1
        else:
            contadorEspacios +=1;

    return  f"tienes {contador} letras y tienesm {contadorNumero} numeros y {contadorEspacios} espacios ";

print (contadorSoloDeLetras(nombreDeAlumno))