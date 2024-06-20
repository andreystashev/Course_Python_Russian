# put your python code here
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

l= []
for i in range(len(a)):
      l.append (str(a[i]+b[i]))
z =' '.join(l)
print(z)



