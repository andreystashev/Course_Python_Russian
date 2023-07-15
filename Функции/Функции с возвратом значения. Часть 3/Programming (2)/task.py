# объявление функции
def solve(a, b, c):
    d = b**2-4*a*c
    if d>0:
        k1= (b*-1+d**0.5)/(2*a)
        k2 = (b*-1-d**0.5)/(2*a)
        if(k1>k2):
            return k2, k1
        else:
            return k1, k2
    elif d==0:
        return -b/(2*a),-b/(2*a)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)