# put your python code here
a = int(input())
l=[]
for i in range(a):
    l.append(input())
f=input().lower()
for i in l:
    if i.lower().find(f)!=-1:
        print(i)



