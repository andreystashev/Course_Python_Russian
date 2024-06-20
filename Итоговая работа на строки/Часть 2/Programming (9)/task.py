
a = input()
f = a.find('f')
if f==-1:
    print(-2)
else:
    a = a.replace('f', 'z', 1)
    l = a.find('f')
    print(l)
