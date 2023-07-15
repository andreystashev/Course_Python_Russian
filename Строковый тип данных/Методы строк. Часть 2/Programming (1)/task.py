# put your python code here
r = input()
a=0
g=0
c=0
t=0

for i in r:
    if i.lower()=="а":
        a+=1
    if i.lower()=="г":
        g+=1
    if i.lower()=="ц":
        c+=1
    if i.lower()=="т":
        t+=1        
print("Аденин:",a)
print("Гуанин:" ,g)
print("Цитозин:" ,c)
print("Тимин:" ,t)

