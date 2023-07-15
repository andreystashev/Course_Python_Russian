# put your python code here
last = 0
r = True
a = int(input())
while a>0:
    if a%10<last:
        r=False
        break
    last = a%10
    a//=10
print("YES" if r else "NO")



