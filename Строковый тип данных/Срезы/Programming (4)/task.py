# put your python code here
a = input()
b=a[:len(a)//2]
f=a[::-1]
c=f[:len(a)//2]
#print(b,c)

print("YES" if b==c else "NO")


