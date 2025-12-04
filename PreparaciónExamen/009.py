listaAlumnos=[ "Luis", "pepe", "Julio"]

try:
    print(listaAlumnos[2])
except IndexError:
    print ("Error al buscar en el índice: No existe")

print("___________________\n")
try:
        print(listaAlumnos[10])
except IndexError:
    print ("Error al buscar en el índice: No existe")