# объявление функции
def is_valid_password(password):
    l = [int(i) for i in password.split(':')]
    if (len(l)!=3):
        return False
    f1 = False
    f2 = True
    f3 = l[2] % 2 == 0
    if str(l[0]) == str(l[0])[::-1]:
        f1 = True

    for i in range(2, l[1]):
        if l[1] % i == 0:
            f2 = False

    return (True if f1 and f2 and f3 else False)


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))