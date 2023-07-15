# put your python code here
a = int(input())
l=[]
for i in range(a):
    l.append(int(input()))
print(max(l))
del l[l.find(max(l))]
#del l[l.min()]
#print(*l,sep='\n')




