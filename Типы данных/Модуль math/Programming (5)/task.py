# put your python code here
a,b,c = float(input()),float(input()),float(input())

d = b**2-4*a*c
if d>0:
    k1= (b*-1+d**0.5)/(2*a)
    k2 = (b*-1-d**0.5)/(2*a)
    if(k1>k2):
        print(k2)
        print(k1)
    else:
        print(k1)
        print(k2)
elif d==0:
    print(-b/(2*a))
else:
    print("Нет корней")


