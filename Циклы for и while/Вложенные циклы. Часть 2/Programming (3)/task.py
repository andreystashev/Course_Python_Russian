# put your python code here
a= int(input())

for i in range(1,a+1):
    value_summ = 1
    for z in range(1,i):
        if i%z==0:
            value_summ+=1
    print(str(i)+('+'*value_summ))
    



