a = [3,4,1,3,5,1,4]
b = [21,54,33,21,77]
c = [0]


def suma_promedios(lista1,lista2,lista3):
    for i in range(len(lista1)): #Ciclo para recorrer el arreglo
        if i == 0 : #Si solo hay un elemento en la lista toma ese para calcular el promedio
           promediores = lista1[i] 
           pivote = lista1[i]
        if i != 0 : #Si hay mas de un solo elemento reliza la sumatoria de los elementos
           promediores = pivote+lista1[i]
           pivote = promediores

    promediores1 = promediores / len(lista1)     #Caclculaelpromedio
    print("Este es el primer promedio "+ str(promediores1))

    for j in range(len(lista2)):
        if j == 0 :
           promediores = lista2[j]
           pivote = lista2[j]
        if j != 0 :
           promediores = pivote+lista2[j]
           pivote = promediores

    promediores2 = promediores / len(lista2)
    print("Este es el segundo promedio " + str(promediores2))

    for k in range(len(lista3)):
        if k == 0 :
           promediores = lista3[k]
           pivote = lista3[k]
        if k != 0:
           promediores = pivote+lista3[k]
           pivote = promediores

    promediores3 = promediores / len(lista3)
    print("Este es el segundo promedio " + str(promediores3))

    sumaTotal = promediores1 + promediores2 + promediores3 #Calcula la suma de todos los promedios en la funcion
    print("Esta es la suma total de los promedios: " + str(sumaTotal))

suma_promedios(a,b,c) #Manda a llamar a la funcion