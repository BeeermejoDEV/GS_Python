""" Recoger un email por consola introducido por el usuario. En una función se debe comprobar que
el correo introducido por el usuario contenga “@” y acabe en “.com” o “.es”. Además, el usuario
solo tendrá tres oportunidades para validar el correo.  """

def validar_email(email):
    if "@" in email and (email.endswith(".com") or email.endswith(".es")):
        return True
    return False
intentos = 3
while intentos > 0:
    email_usuario = input("Introduce tu correo electrónico: ")
    if validar_email(email_usuario):
        print("Correo válido.")
        break
    else:
        intentos -= 1
        print(f"Correo inválido. Te quedan {intentos} intentos.")
else:
    print("Has agotado todas las oportunidades. El correo no es válido.")

