# put your python code here
a = int(input())
summ=0
for i in range(1,a+1):
    if( (i**2)%10==2 or (i**2)%10==8  or (i**2)%10==5  ):
        summ+=i
print(summ)



