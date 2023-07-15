maximum = -100000000
summ = 0
for i in range(10):
    x = int(input())
    if x < 0:
        summ += x
    if x > maximum and x<0:
        maximum = x

if(maximum==-100000000):
    print("NO")
else:
    print(summ)
    print(maximum)