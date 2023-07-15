# put your python code here
a = input()

countThree = 0
countC = 0
countSumm = 0
countMul = 1
countF = 0
for i in a:
    if int(i) == 3:
        countThree += 1
    if int(i) % 2 == 0:
        countC += 1
    if int(i) > 5:
        countSumm += int(i)
    if int(i) > 7:
        countMul *= int(i)
    if int(i) == 0 or int(i) == 5:
        countF += 1
print(countThree)
print(a.count(a[-1]))
print(countC)
print(countSumm)
print(countMul)
print(countF)





