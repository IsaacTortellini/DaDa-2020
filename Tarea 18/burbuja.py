#Reyes Sánchez Daniel Isaac----Método Bubble Sort
Mylist = [6,3,2,1,5,4] #Dada una lista de numeros en desorden

for round in range(1,len(Mylist)): #La lista será recorrida n veces igual al numero de elementos de la lista
    for element in range (len(Mylist) - round): #Se coomparan los elementos en parejas, empezando por el ultimo y penultimo elemento
        if Mylist[element] > Mylist[element + 1]: #Si el elemento en el que nos encontramos es menor al siguiente
            aux = Mylist[element]; #Se almacena el elemento en el que estamos en una variable auxiliar
            Mylist[element]=Mylist[element+1]; #El elemento se intercambia por el siguiente
            Mylist[element+1]=aux; #El siguiente elemento se intercambia con el primero
print(Mylist);            #Se imprime la lista ordenada de menor a mayor