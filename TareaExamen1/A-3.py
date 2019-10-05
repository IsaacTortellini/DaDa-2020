def conteoSuma(arreglo):
    positivos = 0
    pivote = 0
    for i in range(len(arreglo)):
        if arreglo[i] > 0:
            positivos = positivos + 1
        if arreglo[i] < 0:
            sumaNegativos = arreglo[i] + pivote
            pivote = sumaNegativos
    print("El total de numeros positivos es: " + str(positivos))
    print("La suma de numeros negativos es: " + str(sumaNegativos))

lista = [1,2,3,4,5,6,-11,-12,-13,-14,-15]

conteoSuma(lista)

