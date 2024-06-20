# put your python code here
a = int(input())
l=[]
for i in range(a):
    l.append(input())
    
b=int(input())
l2=[]
for i in range(b):
    l2.append(input().lower())

for i in l:
    res = True
    for t in l2:
        if i.lower().find(t)==-1:
            res=False
    if res==True:
        print(i)





