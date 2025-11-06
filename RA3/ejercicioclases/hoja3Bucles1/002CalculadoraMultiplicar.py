"""
Ejercicio 2: Tabla de multiplicar
    Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10. Usa un bucle for
    para generar la tabla. Si el usuario introduce un valor no numérico, muestra un mensaje de
    error usando try-except.
"""


def tabla_multiplicar(numero):
    try:
        i=0
        tabla=[]
        while i<=numero:
            resultado= numero*i
            tabla.append (f"{numero} * {i} = {resultado}")
            i+=1
        
        return tabla

    except:
        resultado= "Error"
        return resultado
    

tabla1 =tabla_multiplicar(2)

for linea in tabla1:
    print(linea)



##Debo practicar todo el tema de Arrays en Python