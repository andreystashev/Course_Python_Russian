# объявление функции
def is_prime(num):
    result = True
    
    for i in range(2,num):
        if num%i==0:
            result = False
    if num<2:
        result=False
    return result



def get_next_prime(num):
    while True:
        num+=1
        if is_prime(num):
            return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))