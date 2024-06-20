# put your python code here
a = int(input())
tek = 0
prev = 1
now = 0
for i in range(a):

    now = prev+tek
    prev = tek
    tek = now
    print(now,end=' ')



