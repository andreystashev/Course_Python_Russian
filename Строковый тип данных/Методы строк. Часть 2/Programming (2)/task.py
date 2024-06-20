# put your python code here
n = int(input())
s = 0
for i in range(n):
    x = input()
    if x.count('11')>=3:
        s+=1
print(s)


