i = 0
n=1
h = ''

l = 0

for l in range(19):
    
    if n%2 != 0 and n<20 :
        h += ' %i' %n
        print(h)
    n +=1