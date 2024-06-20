# put your python code here
a=1000
b=0
c=0
while(True):
    b=a/100*8
    a+=b
    c+=1
    print(c)
    if a>=3000:
        break
print(c)