# put your python code here
a = input()
num = 0
char = 0
for i in a:
    z = a.count(i)
    if z>=num:
        num=z
        char = i
print(char)
    



