
lista1 = [0,2,4,6,1,9]
numero = 2

def divisible(lista,divisor):

    for i in range (0,len(lista)):
        if lista[i] != 0:
           if lista[i] % divisor == 0:
               print(" " + str(lista[i]))
      
divisible(lista1,numero)
