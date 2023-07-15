# put your python code here
n = int(input())
if n>36 or n<0:
    print("ошибка ввода")
elif n==0:
    print("зеленый")
elif n>0 and n<11:
    if n%2==0:
        print("черный")
    else:
        print("красный")
elif n>10 and n<19:
    if n%2==0:
        print("красный")
    else:
        print("черный")
elif n>18 and n<29:
    if n%2==0:
        print("черный")
    else:
        print("красный")
elif n>28 and n<37:
    if n%2==0:
        print("красный")
    else:
        print("черный")

