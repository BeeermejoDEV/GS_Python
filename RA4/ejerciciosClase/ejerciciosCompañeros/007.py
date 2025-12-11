""" Pedir por teclado una cadena de texto y “analizarla” con distintas funciones.
Deberá contar la longitud total, contar las letras (mirar str.isaplha()), contar los números, contar
los caracteres especiales y contar los espacios """

def analizar_cadena(cadena):
    longitud = len(cadena)
    letras = sum(1 for c in cadena if c.isalpha())
    numeros = sum(1 for c in cadena if c.isdigit())
    especiales = sum(1 for c in cadena if not c.isalnum() and not c.isspace())
    espacios = sum(1 for c in cadena if c.isspace())
    return longitud, letras, numeros, especiales, espacios  
# Ejemplo de uso
cadena_usuario = input("Introduce una cadena de texto: ")
longitud, letras, numeros, especiales, espacios = analizar_cadena(cadena_usuario)
print(f"Longitud total: {longitud}")
print(f"Número de letras: {letras}")
print(f"Número de números: {numeros}")
print(f"Número de caracteres especiales: {especiales}")
print(f"Número de espacios: {espacios}")
