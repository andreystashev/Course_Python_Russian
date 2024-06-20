# put your python code here
def sq(num):
    summ=0
    while num>0:
        summ+=num%10
        num//=10
    return summ
        
a = int(input())
while a>=10:
    a=sq(a)
print(a)
    


