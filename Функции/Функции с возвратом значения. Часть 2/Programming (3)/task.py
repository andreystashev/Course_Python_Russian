# объявление функции
def is_password_good(password):
    lenth = len(password)>7
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = "abcdefghijklmnopqrstuvwxyz"
    numb = "1234567890"
    bg = False
    sm = False
    nm = False
    for i in password:
        if i in big:
            bg=True
        if i in small:
            sm = True
        if i in numb:
            nm = True
            
        
    return lenth and bg and sm and nm

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))