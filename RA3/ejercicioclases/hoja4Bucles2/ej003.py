
def primer_multiplo():
    for num in range(81, 200):
        if num % 7 != 0:   # si no es múltiplo de 7, saltamos
            continue
        else:
            print(f"El primer múltiplo de 7 entre 80 y 200 es: {num}")
            break

# Llamada a la función
primer_multiplo()   