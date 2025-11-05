"""
Ejercicio 3: Crear usuario con lista
Crea una función llamada `crear_usuario` que reciba los siguientes argumentos por palabra clave:
    - nombre (str)
    - email (str)
    - activo (bool), con valor por defecto True
La función debe devolver una lista sólo de los usuarios activos con los datos del usuario en
el orden: [nombre, email, activo].

"""

def crear_usuario(nombre, email, activo=True):
    ## aqui demuestra que si activo es true muestra
    if activo:
        return [nombre, email, activo]
    else:
        return None


usu1= crear_usuario (nombre="David", email="dav@gmail.com")
usu2= crear_usuario (nombre="David", email="dav@gmail.com",activo=False )
print (usu1,usu2)
