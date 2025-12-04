def saludo (nombre, mensaje ="Hola"):
    print (mensaje, nombre)

nombre= input ("Introduzca su nombre: \n")
mensaje= input("introduce un mensaje personalizado: \n")

saludo(nombre)
print("_______________ \n")
saludo(nombre, mensaje)