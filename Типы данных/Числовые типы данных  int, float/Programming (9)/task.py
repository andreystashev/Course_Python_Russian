# put your python code here
a = int(input())
b = [a//100,a//10%10,a%10]
b.sort()
#print(b[2],b[0],b[1])
print("Число интересное" if (b[2]-b[0]==b[1]) else "Число неинтересное")



