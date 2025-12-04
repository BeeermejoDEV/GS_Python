lista=[]
respuesta=""
while respuesta !="salir":
    respuesta= input("Introduce un nombre a añadir a la lista \n")

    if respuesta =="salir":
        break
    else:
        lista.append(respuesta)

for nombre in lista:
    print(nombre)
