a = int(input())
l = []
for i in range(a):
    x=input()
    l.append(x)
c = int(input())
for i in range(a):
    if(len(l[i])>=c):
        print(l[i][c-1],sep='',end='')





