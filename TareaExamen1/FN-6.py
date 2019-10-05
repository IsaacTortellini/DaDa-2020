a=[4,3,2,1]
 
def suma_resta(lista):
    
    suma = 0
    pivote = 0

    for i in range (len(lista)-1):
        
        resta = lista[i] - lista[i+1]
        suma = resta + pivote
        pivote = suma
    print("Total " + str(suma))

suma_resta(a)

