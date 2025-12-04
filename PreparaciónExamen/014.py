def suma_varios(*numeros):
    total = 0
    for i in numeros:
        total += i
    return total

print("la suma es: ", suma_varios(2,3,1,2))
    
