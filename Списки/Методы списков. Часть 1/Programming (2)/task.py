# put your python code here
abc = 'abcdefghijklmnopqrstuvwxyz'
l=[]
for i in range(26):
    s = str()
    for z in range(i+1):
        s+=abc[i]
    l.append(s)
print(l)       



