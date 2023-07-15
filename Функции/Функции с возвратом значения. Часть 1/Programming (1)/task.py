# объявление функции
def get_days(month):
    a=(1,3,5,7,8,10,12)
    if month == 2:
        return 28
    elif month in a:
        return 31
    else:
        return 30
       

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))