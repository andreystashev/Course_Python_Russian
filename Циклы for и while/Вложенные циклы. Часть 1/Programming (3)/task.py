# put your python code here
def draw_triangle(fill, base):
    half = base//2
    for i in range(1,half+1):
        print(fill*i)
    print(fill*(half+1))
    for i in range(half,0,-1):
        print(fill*i)
        

# считываем данные
#fill = input()
base = int(input())

# вызываем функцию
draw_triangle("*", base)



