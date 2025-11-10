# Función para calcular y mostrar el capital año a año
def calcular_inversion(cantidad, interes, años):
    for i in range(1, años + 1):
        cantidad *= (1 + interes / 100)
        print(f"Año {i}: capital = {cantidad:.2f} €")

# Solicitar datos al usuario
capital_inicial = float(input("Cantidad a invertir (€): "))
interes_anual = float(input("Interés anual (%): "))
num_años = int(input("Número de años: "))

# Llamada a la función
calcular_inversion(capital_inicial, interes_anual, num_años)