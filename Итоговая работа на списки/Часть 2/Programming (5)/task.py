# put your python code here
a = [i for i in input().split()]

l= []
for i in a:
    t=i[1:]
    t+=i[0]+'ки'
    l.append(t)
    
    
z =' '.join(l)
print(z)




