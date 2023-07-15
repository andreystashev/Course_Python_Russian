# put your python code here
t = input().lower().split()
a= t.count('a')

c= t.count('an')

e= t.count('the')

print('Общее количество артиклей:',a+c+e)
