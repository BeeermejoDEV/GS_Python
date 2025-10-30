PrecioTotal=0
contador=0
contadorIntentos=0

while True:
    numUsu=float(input("Introduce un numero \n"))
    if numUsu!=9999.99:
        PrecioTotal=PrecioTotal+numUsu


    try:
        if numUsu>=0:
            contadorIntentos=contadorIntentos+1
            #print ("numeros introducidos: ",contadorIntentos)    
            if numUsu >=10:
                print (numUsu)
                contador=contador+1
                #print("Precios de mas de 10 euros: ",contador)
            


        else:
            print ("Debe ser numero positivo")

        if numUsu ==9999.99:
            print ("Has introducido 9999.99 ")
            contador = contador-1 ##restamos el contador
            contadorIntentos=contadorIntentos-1 ##Restamos el contador de intentos en 1
            print ("Contador de numeros que superaban 10 euros: ",contador)
            print ("Media de todos los productos: ",PrecioTotal/contadorIntentos)
            print ("Saliendo del sistema")
            break
    except:
        print ("Debe ser mayor o igual que 0")

