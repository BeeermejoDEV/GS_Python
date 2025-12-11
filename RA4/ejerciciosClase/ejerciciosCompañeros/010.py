""" Recibir dos cadenas de caracteres y contar sus vocales para después sumarlas.
por otra parte combinar las dos cadenas y remplazar cada carácter que este en una
posición impar por una “C”. """

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = sum(1 for char in cadena if char in vocales)
    return contador 
# Recibir dos cadenas de caracteres
cadena1 = input("Introduce la primera cadena de texto: ")
cadena2 = input("Introduce la segunda cadena de texto: ")
# Contar vocales en ambas cadenas
vocales_cadena1 = contar_vocales(cadena1)
vocales_cadena2 = contar_vocales(cadena2)
total_vocales = vocales_cadena1 + vocales_cadena2
print(f"Número total de vocales en ambas cadenas: {total_vocales}")
# Combinar las dos cadenas
cadena_combinada = cadena1 + cadena2
# Reemplazar caracteres en posiciones impares por "C"
cadena_modificada = ''.join('C' if i % 2 != 0 else char
    for i, char in enumerate(cadena_combinada))
print(f"Cadena combinada y modificada: {cadena_modificada}")
    