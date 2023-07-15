# put your python code here
summ=0
calc=0
mul = 1
mid = 0
first = 0
first_last_summ = 0
a = int(input())
while a>0:
    summ+=a%10
    calc+=1
    mul*=a%10
    if calc==1:
        first_last_summ+=a%10
    
    if a<10:
        first_last_summ+=a%10
        first =a%10
    a//=10
mid=summ/calc

print(summ)
print(calc)
print(mul)
print(mid)
print(first)
print(first_last_summ)   



