a = input()
summP=0
summM=0
for i in range(len(a)):
    if(a[i]=='+'):
        summP+=1
    if(a[i]=='*'):
        summM+=1   
    
print("Символ + встречается",summP,"раз")   
print("Символ * встречается",summM,"раз")       

