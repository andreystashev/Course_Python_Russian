def is_magic(date):
    l = date.split('.')
    #print(l)
    #print(l[0],l[1],l[2])
    return int(l[0])*int(l[1]) ==int(l[2])%100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))