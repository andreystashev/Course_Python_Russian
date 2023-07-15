# put your python code here

a,b,c=int(input()),int(input()),int(input())
if(a==b and a!=c or a==c and a!=b or b==c and b!=a):
    print("Равнобедренный")
elif(a!=b and b!=c and a!=b):
    print("Разносторонний")
else:
    print("Равносторонний")



