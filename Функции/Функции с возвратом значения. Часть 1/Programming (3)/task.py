# объявление функции
def get_factors(num):
    l=[]
    for i in range (1,num+1):
        if num%i==0:
            l.append(i)
    return l

def number_of_factors(num):
    return len(get_factors(num))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))