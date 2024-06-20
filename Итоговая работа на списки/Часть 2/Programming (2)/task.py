# put your python code here
a = [int(i) for i in input().split()]
b= str()
summ=0

for i in a:
    summ+=i
    b+=str(i)
    b+='+'
t =b[:-1]
t+='='+str(summ)
print(t)


