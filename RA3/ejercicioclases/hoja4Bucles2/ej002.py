def cuenta_atras(numero):
    for i in range(numero, -1, -1):
        # end="" evita el salto de línea, y la coma separa los números
        if i > 0:
            print(i, end=", ")
        else:
            print(i)

# Solicitar número al usuario
n = int(input("Introduce un número entero positivo: "))

if n >= 0:
    cuenta_atras(n)
else:
    print("ERROR!!! El número debe ser positivo.")