# put your python code here
a = int(input())
d1=a//100
d2=a//10 %10
d3=a%10
print(d1,d2,d3,sep='')
print(d1,d3,d2,sep='')
print(d2,d1,d3,sep='')
print(d2,d3,d1,sep='')
print(d3,d1,d2,sep='')
print(d3,d2,d1,sep='')

