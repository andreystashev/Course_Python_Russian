# put your python code here
import math
a = int(input())
summ=1
for i in range(2,a+1):
    
        summ+=1/i
print(summ-math.log(a))



