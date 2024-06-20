# put your python code here

        
a = int(input())
summ = 0
for i in range(1,a+1):
    fact = 1
    for z in range(1,i+1):
        fact*=z
    summ+=fact
        
    

print(summ)
    



