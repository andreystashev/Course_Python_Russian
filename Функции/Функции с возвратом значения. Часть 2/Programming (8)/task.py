# объявление функции
def convert_to_python_case(text):
    t2 = str()
    for i in text:
        if i.isupper():
            t2+='_'+i.lower()
        else:
            t2+=i
    return t2[1:]

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))