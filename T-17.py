
arreglo = [6,5,4,3,2,1]

def multiplicacion(arr):
    contador=1
    for i in range(len(arr)): 

        resultado=contador*arr[i] #operación básica
        contador=resultado

    print("El resultado de la multiplicación de los elementos del arreglo "+ str(arreglo) + "   Es:"+ str(resultado))

multiplicacion(arreglo)
