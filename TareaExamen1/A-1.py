
# En una lista de numeros enteros de 0 al 9, encontrar cual falta dentro del arreglo

lista = [1,2,3,4,5,6,7,8,9,0]
sumaTotal = 45
i = 0
sumaLista = 0


def numeroFaltante(listas):

    pivote = 0
    hayZero = False

    for i in range (len(listas)):

        sumaLista = pivote + listas[i]
        pivote = sumaLista
    
    print("Esta es la suma de la lista: " + str(sumaLista))

    if sumaLista != sumaTotal:
        numeroFaltante = sumaTotal - sumaLista
        print("El numero faltante es: " + str(numeroFaltante))
    
    for i in range (len(lista)):
        if listas[i] == 0:
            hayZero = True
           
    if hayZero == False:
        print("Falta el 0")

        

numeroFaltante(lista)
    