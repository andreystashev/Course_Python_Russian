# put your python code here
n = int(input())
a = input()
l=str()
for i in a:
    if ord(i)-n<97:
        t =ord(i)-97
        z=n-t
        r = 123-z
        l+=chr(r)
    else:
        l+=chr(ord(i)-n)
        
print(l)
        
    
    



