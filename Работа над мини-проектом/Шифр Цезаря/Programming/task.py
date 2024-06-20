# put your python code here
def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()
a = input().split()
z_str=str()
for i in a:
    w_count = 0
    new_s=str()
    for z in i:
        if z.isalpha():
            w_count+=1
    for z in i:
        if z.isalpha():
            new_s+=sdvig(z,w_count)
        else:
            new_s+=z
    
    z_str+=new_s+' '
print(z_str)
        
        



