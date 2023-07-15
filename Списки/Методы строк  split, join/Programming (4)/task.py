# put your python code here
a = input().split(".")
r = True
for i in a:
    if not 0<=int(i)<=255:
        r=False
print("ДА" if r else "НЕТ")        



