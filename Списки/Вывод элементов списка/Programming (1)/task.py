# put your python code here
a = int(input())
l=[]
for i in range(a):
    l.append(int(input()))
    
print(*l,sep='\n')
print()
for i in range(a):
    print(l[i]**2+2*l[i]+1)

          



