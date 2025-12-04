nums = [2, 5, 8, 9, 10, 12, 15, 20]

numsMayor10=[]
numsPares=[]

for numero in nums:
    if numero%2==0:
        numsPares.append(numero)
    
    if numero>=10:
        numsMayor10.append(numero)

print("Numeros pares: ")
for numero in numsPares:
    print (numero)

print ("Numeros mayores que 10: ")
for numero in numsMayor10:
    print (numero)