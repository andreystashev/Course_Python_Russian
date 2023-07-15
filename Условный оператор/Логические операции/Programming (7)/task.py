# put your python code here
x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())

#if((x1+1==x2 or x1-1==x2 or y1+1==y2 or y1-1==y2) ):

if(x2>x1+1 or x2<x1-1 or y2>y1+1 or y2<y1-1):
    print("NO")
else:
    print("YES")




