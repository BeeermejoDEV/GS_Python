#X²,    √X,     ,X % 5,     X / 0 → esto debe darte error, tranquilo, es parte del ejercicio
import math

entradaUsu= int(input("Introduzca un numero: "))

print("X*X= ", math.pow(entradaUsu, 2))
print("√X= ", math.sqrt(entradaUsu))
print("X % 5", entradaUsu%5)
print("X/0", entradaUsu/0)