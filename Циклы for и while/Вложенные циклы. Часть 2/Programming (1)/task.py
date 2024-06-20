# put your python code here
a=int(input())

for i in range(1,a+1):
    for z in range(i):
        print(z+1,end='')
    for x in range(z,0,-1):
        print(x,end='')
    print()



