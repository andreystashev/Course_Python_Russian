# put your python code here
a,b = int(input()),int(input())
max_summ = 0
max_num = 0
for i in range(a,b+1):
    value_summ = 0
    for z in range(1,i+2):
        if i%z==0:
            value_summ+=z
    if value_summ>=max_summ:
        max_summ=value_summ
        max_num=i
print(max_num,max_summ)
    




