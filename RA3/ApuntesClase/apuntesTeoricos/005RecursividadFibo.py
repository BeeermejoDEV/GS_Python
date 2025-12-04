#funcion recursiva
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

#ejemplo de uso
n = input("Ingrese el valor de n para calcular el n-ésimo número de Fibonacci: ")
n = int(n)

print(f"El {n}º número de Fibonacci es: {fibonacci(n)}")
#funcion iterativa
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


#ejemplo de uso
print(f"El {n}º número de Fibonacci (iterativo) es: {fibonacci_iterativo(n)}")  