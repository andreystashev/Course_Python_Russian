# put your python code here
a = input()
summP=0
summM=0
for i in range(len(a)):
    if(a[i] in 'аоуыиэяюёеАУОЫИЭЯЮЁЕ'):
        summP+=1
    if(a[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'):
        summM+=1   
    
print("Количество гласных букв равно",summP)   
print("Количество согласных букв равно",summM)      



