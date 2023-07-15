# put your python code here
a = int (input())
ma=0
mi=9
while a>0:
        if(a%10<mi):
            mi=a%10
        if(a%10>ma):
            ma=a%10
        a//=10
print("Максимальная цифра равна" ,ma)
print('Минимальная цифра равна' ,mi)



