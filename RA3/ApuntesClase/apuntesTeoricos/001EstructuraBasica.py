"""
Estructura básica de las funciones:
"""
valor_opcional=0


def nombreFuncion(parametroOpcional):
    #Codigo...
    return valor_opcional +12
#Def                ⇢ estamos definiendo que es una funcion:
#NombreFuncion      ⇢ Ponemos un nombre a la funcion.
#parametroOpcional  ⇢ Podemos introducir parametros (un nombre por ejemplo)
#return             ⇢ Puede (opcional) devolver un valor.



print("_________________________________________________")
print("_________________________________________________")
print ("Funcion con parametros: \n")


## Usos :Cuando la función depende de un valor variable \\\ Cuando quieres reutilizar la función muchas veces \\\ Cuando los datos vienen de otra parte del programa
def saludar(nombre):
    print (f"Hola! {nombre}") #Creamos una funcion que nosotros danadole un parametro, devuelve un saludo personalizado

saludar(nombre = input("Escribe tu nombre!"))


print("_________________________________________________")
print("_________________________________________________")
print ("Funcion que devuelve un return valor")

## Usos: Cálculos o resultados numéricos \\\ Procesar texto o cadenas \\\ Comprobar condiciones o estados \\\ Reutilizar resultados en otras operaciones
def sumar (a,b):
    return a+b

num1= float(input("Introduzca el valor de num1: \n"))
num2= float(input("introduzca el valor de num2: \n"))

resultado= sumar(num1,num2)
print(f"el resultado es: {resultado}")


print("_________________________________________________")
print("_________________________________________________")
print("Resultado VOID... ")

### Usos: Mostrar mensajes al usuario \\\ Registrar o guardar información \\\ Interacción con el usuario

def mensajeSalida():
    print("Saliendo del sistema!")

mensajeSalida()


print("_________________________________________________")
print("_________________________________________________")
print("Validaciones de datos: \n")

##combinar funciones y condicionales para crear validaciones

def es_Par(num):
    if num%2==0:      return True
    else:               return False

num= int(input ("Introduzca un numero para verificar si es par o impar: "))
es_Par(num)
        