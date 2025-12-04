import random

# Asignamos número a cada participante
ganadores = {
    1: "Ana",
    2: "Luis",
    3: "María",
    4: "Pedro",
    5: "Sofía",
    6: "Julio", 
    7: "Pacheco",
    8: "Bermejo"
}

# Elegimos un número al azar
numero_ganador = random.randint(1, len(ganadores))

# Lo usamos para obtener al ganador
print("Número ganador:", numero_ganador)
print("El ganador es:", ganadores[numero_ganador])
