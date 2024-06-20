# объявление функции
def is_correct_bracket(text):
    n=0
    for i in text:
        if i == '(':
            n+=1
        elif i == ')':
            n-=1
            if(n<0):
                return False
    if n!=0:
        return False
    else:
        return True
        
        

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))