"""
Ejercicio 8: Generar tabla de multiplicar
    Crea una función llamada `tabla_multiplicar` que reciba:
        - numero (int)
        - hasta (int), como argumento por palabra clave, con valor por defecto 10
    La función debe devolver una lista con la tabla de multiplicar del número hasta el valor
    indicado.
"""

### Funciona, pero me pide que devuelva una lista...!!!

def tabla_multiplicar(numero,hastaNum=10):
    i=0
    while i<= hastaNum:
        resultado= numero*i
        print (numero , " x ", i ," = " , resultado)
        i+=1

num1= int (input ("Escribe el numero a multiplicar: "))
num2= int (input("Escibe cuantas veces debe multiplicarse: "))
tabla_multiplicar(num1,num2)
    


##version corregida con Gpeto pero adaptado por mi

def tabla_mult(nume, hasta=10):
    tabla=[]
    for i in range(hasta + 1):
        resultado = nume * i
        tabla.append(f"{nume} x {i} = {resultado}")
    return tabla
    

numero1 = int(input("Escribe el número a multiplicar: "))
numero2 = (input("¿Hasta qué número deseas multiplicar? "))

if numero2 == "": numero2=10
else: int (numero2)


tabla = tabla_mult(numero1,numero2)



for linea in tabla:
    print(linea)
