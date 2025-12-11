""" Crear una función que reciba un DNI por parámetro y valide si es correcto.
El DNI debe tener 8 números y 1 letra, y la letra debe coincidir con la letra oficial obtenida con la
fórmula del DNI (número % 23 usando la cadena "TRWAGMYFPDXBNJZSQVHLCKE").
La función debe devolver True si el DNI es válido y False si no lo es.
Después, probar la función con varios DNIs.  """
def validar_dni(dni):
    letras_oficiales = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(dni) != 9:
        return False
    numero = dni[:-1]
    letra = dni[-1].upper()
    if not numero.isdigit():
        return False
    indice = int(numero) % 23
    letra_correcta = letras_oficiales[indice]
    return letra == letra_correcta
# Ejemplo de uso
dni_usuario = input("Introduce tu DNI (8 números y 1 letra): ")
if validar_dni(dni_usuario):
    print("DNI válido.")
else:
    print("DNI inválido.")

