# put your python code here
a,b = int(input()),int(input())

for i in range(a,b+1):
    count = 0
    for z in range(2,i):
        if i%z==0:
            count+=1
    if count==0 and i!=1:
        print(i)
        
    




