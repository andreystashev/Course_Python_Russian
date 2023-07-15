# put your python code here
a = input()
b=str()
c=str()
if(len(a)%2==0):
    b=a[:len(a)//2]
    c=a[len(a)//2:]
    
else:
    b=a[:len(a)//2+1]
    c=a[len(a)//2+1:]


print(c,b,sep="")

#print("YES" if b==c else "NO")



