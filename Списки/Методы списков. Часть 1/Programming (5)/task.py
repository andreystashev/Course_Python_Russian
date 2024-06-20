# put your python code here
a = int(input())
l=[]
for i in range(a):
    l.append(int(input()))

l2=[]
for i in range(len(l)-1):
    l2.append(l[i]+l[i+1])
print(l2)



