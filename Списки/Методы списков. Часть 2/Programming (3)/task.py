# put your python code here
a = input()
num = int(a[1:])
l= [input() for i in range(num)]
for i in l:
    if i.find('#')!=-1:
        print(i[:i.find('#')].rstrip())
    else:
        print(i)
    



