# put your python code here
a=input().split()
aa =[]
for i in a:
    aa.append(int(i))

v=aa.index(max(aa))
z=aa.index(min(aa))

aa[v],aa[z]=min(aa),max(aa)
a.clear()
for i in aa:
    a.append(str(i))
#print(max(a),min(a))

#,min(a)= min(a),max(a)
x=' '.join(a)
print(x)


