#Es una forma de combinar paramtros****

#Puedo pedir todos los nombres
def nombres( greetings, *names):
    for name in names:
        print (greetings , name)



#Puedo coger un nombre concreto
def apellidos( *apellidos):
    print (apellidos[1])

nombres ("hello", "Raquel", "pachecoGay", "alexMalpe")
apellidos ("Bermejo", "lorca", "Malpelo")


##El *parametro[0] coge el valor para por ejemplo, saludo:


def sumaNums (*numbers):
    total=0
    for number in numbers:
        total=number+total
    return total


#sumaNums(4,5,1,2,3)    --> no declaramos, si no directamente para llamarla

print (sumaNums(2,3,4,5))



