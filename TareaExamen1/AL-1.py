



for i in range (1,101):
    esPrimo = True

    if i < 2:
       esPrimo = False 

    for n in range(2,i):
        if i % n == 0:
            esPrimo = False
            
    if esPrimo == True:
        print("Numero primo " + str(i))
    if esPrimo == False:
        print("No primo "+ str(i))

        
        