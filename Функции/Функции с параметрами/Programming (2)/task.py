# объявление функции
def print_digit_sum(num):
    summ=0
    while num>0:
        summ+=num%10
        num//=10
    print(summ)
        

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)