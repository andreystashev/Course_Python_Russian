# put your python code here
l = [int(i) for i in input().split()]
t=0

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            t+=1
print(t)



