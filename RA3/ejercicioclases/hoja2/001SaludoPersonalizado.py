"""
Ejercicio 1: Saludo personalizado
Crea una función llamada saludar que reciba dos argumentos por palabra clave:
    - nombre (str)
    - saludo (str), con valor por defecto "Hola"
La función debe devolver una cadena con el saludo seguido del nombre.
"""
def saludar (nombre, saludo):
    return "hola " + saludo + ""+ nombre ##en caso de que no queramos que devuelva saludo, no ponemos nada en saludo

## Palabra clave??? decimos que quiere que diga??

mensaje=    saludar(nombre="david",saludo=" ") ## Damos los datos nosotros 
print(mensaje)