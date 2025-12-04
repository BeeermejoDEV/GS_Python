def calcular_precio_final(precio, iva=21):
    return round(precio*(1+(iva/100)),3)


print("El precio final es de: ",calcular_precio_final(100))
print("El precio final es de: ", calcular_precio_final(100,10))

def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. salir")

mostrar_menu()


def sumar_todos(*numeros):
    total=0
    for numero in numeros:
        total+=numero
    return total

print(sumar_todos(7,4,5,4,10))
