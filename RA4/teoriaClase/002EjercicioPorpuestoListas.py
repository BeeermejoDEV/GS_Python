numeros = [3, 7, 2, 9, 4, 1, 8]

""" Muestre la lista original

Calcule y muestre:

El número mayor

El número menor

La suma de todos los números

Muestre cuántos números son pares """

print("Lista original:", numeros)
mayor = max(numeros)
menor = min(numeros)
suma = sum(numeros)
pares = len([num for num in numeros if num % 2 == 0])
print("Número mayor:", mayor)
print("Número menor:", menor)
print("Suma de todos los números:", suma)
print("Cantidad de números pares:", pares)
