"""
Reutilizacion de codigo:
"""

def espar(num):
    return num%2==0

for i in range (1,11):
    print (f"es par el numero? {i} == {espar(i)}")