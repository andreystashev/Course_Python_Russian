# put your python code here
a=int(input())
summ=0

twenty_five = a//25
ten = (a-twenty_five*25)//10
five = (a-twenty_five*25-ten*10)//5
one = (a-twenty_five*25-ten*10-five*5)//1
summ=twenty_five+ten+five+one
#print(twenty_five,ten,five,one)    
    
print(summ)






