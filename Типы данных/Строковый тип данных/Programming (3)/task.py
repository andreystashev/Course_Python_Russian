# put your python code here
a,b,c=input(),input(),input()
print(a if len(a)<len(b) and len(a)<len(c) else (b if len(b)<len(a) and len(b)<len(c) else c) )
print(a if len(a)>len(b) and len(a)>len(c) else (b if len(b)>len(a) and len(b)>len(c) else c) )



