# put your python code here
a = input()
summ=0
for i in range(len(a)):
    if(a[i]=='1' or a[i]=='2' or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='8' or a[i]=='9' or a[i]=='0'):
        summ+=1
        break
    
print("Цифра" if summ>0 else "Цифр нет")   
    




