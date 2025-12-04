def area_rectangulo (base, altura):
    return base*altura

def pedirDatos():
    datoUsu= int(input("Introduzca el dato: "))
    return datoUsu

base= pedirDatos()
altura= pedirDatos()

print ("El area del triangulo es: ", area_rectangulo(base, altura))