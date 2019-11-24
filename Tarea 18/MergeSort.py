#Reyes Sánchez Daniel Isaac----Método MergeSort
myList = [6,3,2,1,5,4]
def mergeSort(myList): #Defino la función mergesort
    if len(myList) > 1: #Compruebo si la lista tiene más de 2 elementos
        mid = len(myList) / 2
        left = myList[:int(mid)] #Separo mi lista en 2 listas auxiliares
        right = myList[int(mid):]

        #Aplico la función mergesort en cada lista auxiliar
        mergeSort(left)
        mergeSort(right)

        # Declaro 2 variables auxiliares para desplazarme dentro de cada lista o mitad
        i = 0
        j = 0
        
        # Declaro la variable auxiliar para la lista principal
        k = 0
        
        while i < len(left) and j < len(right): #Se ejecuta para ambas listas o mitades
            if left[i] < right[j]: #Se comparan los elementos de ambasmitades
              
              myList[k] = left[i] #Si el elemento de la izquierda es menor al de la derecha se coloca en la lista principal
              
              i += 1 #Siguiente numero
            else:
                myList[k] = right[j] #si el elemento de la derecha es menor al de la izquierda se coloca en la lista principal
                j += 1
            
            k += 1  #Siguiente numero

        # Se hace lo mismo para todos los valores restantes 
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

mergeSort(myList)
print(myList)