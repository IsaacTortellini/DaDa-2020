

num=int(input('Introduce un numero igual o menor a 10 para saber su factorial: '))
print('El numero introducido fue: ',num)
fact = 1
if num<=10:
    for i in range (num):
         fact *= num
         num-=1
    
    print('Su factorial es: ',fact)
elif num == 0 or num==1:
    print('Su factorial es: 1') 
else :
    print('Error el número debe ser menor a 10')



