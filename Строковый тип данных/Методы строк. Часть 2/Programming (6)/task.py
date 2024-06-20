# put your python code here
a = input()
if a.find('f')==-1:
    print("NO")
else:
    first =a.find('f')
    z=a[:a.find('f')]
    z+='s'
    z+=a[a.find('f')+1:]
    if z.find('f')!=-1:
        last = z.rfind('f')
        print(first,last)
    else:
        print(first)


