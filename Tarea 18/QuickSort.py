#Reyes Sánchez Daniel Isaac----Método Quick Sort
myList=[6,3,2,1,5,4]
def quicksort(lista):#Se define la función quicksort
  if len(lista) == 0: #Se comprueba que no sea una lista vacía
    return []

  left = [] #Defino listas auxiliares
  right = []
  pivot = lista[0] # El primer elemento de la lista será el pivote

  for element in lista[1:]: #Se comparan los elementos con el pivote
    if element < pivot:
      
      left.append(element)# Si el elemento es menor al pivote, se añade a la izquierda
    else:
      
      right.append(element)# Si es mayor, a la derecha

  return quicksort(left) + [pivot] + quicksort(right) #Se aplica la funcion quick sort a cada nueva lista y se concatenan


print(quicksort(myList))
