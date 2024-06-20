# put your python code here
a=input()
if(len(a)==12):
    if(a[3]=='-' and a[7]=='-'):
        a=a.replace('-',"",2)
        if a.isdigit():
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    
elif(len(a)==14):
    if(a[1]=='-' and a[5]=='-' and a[9]=='-' and a[0]=='7'):
        a=a.replace('-',"",3)
        if a.isdigit():
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")

