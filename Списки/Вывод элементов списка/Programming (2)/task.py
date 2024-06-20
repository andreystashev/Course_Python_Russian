# put your python code here
a = int(input())
l=[]
for i in range(a):
    l.append(int(input()))
    
#print(max(l),min(l),"fff")
for i in l:
    
    if not(i==max(l) or i==min(l)):
        print(i)






