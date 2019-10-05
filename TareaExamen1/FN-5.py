
def buscaLider(lista):
    
    pivote = 0
    numeroMayor = 0
    for j in range (len (lista)):
            if lista[j] > numeroMayor:
                numeroMayor = lista[j]

    for i in range(len(lista)):
        if lista[i] != numeroMayor:
           sumaPromedio = lista[i] + pivote
           pivote = sumaPromedio

    promedio = sumaPromedio / (len(lista)-1)
  
    if numeroMayor <= promedio:
        print("No hay numero lider")
    else:
        print("El numero lider es: " + str(numeroMayor))

a = [3,2,10,1]
buscaLider(a)