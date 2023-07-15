# put your python code here
a = int(input())
summ=0
for i in range(1,a+1):
    
    if i%2==0:
        i*=-1
    summ+=i

print(summ)



