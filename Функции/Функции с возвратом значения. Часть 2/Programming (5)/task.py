# объявление функции
def is_palindrome(text):
    t2=str()
    for i in text:
        if i.isdigit() or i.isalpha():
            t2+=i.lower()
    if t2==t2[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))