# put your python code here
l=[]
for i in range(int(input())):
    l+=[int(i) for i in input().split()]
l.sort()
print(*l)



