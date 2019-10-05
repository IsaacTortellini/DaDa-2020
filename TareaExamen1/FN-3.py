
lista_nueva = []
lista_original=[9,3,1,3,2,9]
conta=0
for j in range (len(lista_original)):
    conta=0
    for i in range (0,len(lista_original)):
        if( lista_original[j]==lista_original[i]):
            conta=conta+1 
    if(conta==1):   
        lista_nueva.append(lista_original[j])
print(lista_nueva)