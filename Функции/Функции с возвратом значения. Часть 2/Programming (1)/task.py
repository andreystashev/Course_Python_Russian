# объявление функции
def is_prime(num):
    result = True
    
    for i in range(2,num):
        if num%i==0:
            result = False
    if num<2:
        result=False
    return result

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))