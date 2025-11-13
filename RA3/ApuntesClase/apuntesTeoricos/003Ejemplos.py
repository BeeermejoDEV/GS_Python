def maximoLista (*numbers):
    if len (numbers)==0:
        return None
    
    max_num= numbers[0]
    for number in numbers:
        if number>max_num:
            max_num = numbers[number]
    return max_num


print(maximoLista(2,3,1,10,9))

print("_________________")
#factor multiplicador, y luego sume todo

def multiplicar (operador, *numbers):
    suma=0
    for number in numbers:
        print (operador*number)
        suma= suma+(operador*number)
    print("El total de la suma es: ",suma)

multiplicar (2,6,10,12)


##pizzeria (madePizza) me tiene que devolver tamaño, y ingredientes(pido ingredientes)

def madePizzero (porciones:int=8, *ingredientes): ##para pedir que sea un int
    pizza=[]

    if not isinstance (porciones, int):
        raise TypeError ("Error, tienes que meter un numero en porciones")
    

    for ingrediente in ingredientes:
        pizza.append(ingrediente)

    print("Tendrás una pizza con :", porciones, " porciones y los ingredientes son: " ,pizza)

madePizzero("pepe","salami", "bacon", "queso")

##añadir datos de ingredientes 
##ganador entre varias personas de forma aleatoria.