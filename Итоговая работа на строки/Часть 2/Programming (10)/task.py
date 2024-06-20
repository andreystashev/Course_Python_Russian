a = input()
f = a.find('h')
l = a.rfind('h')
z = a[:f]
z+=''.join(reversed(a[f:l+1]))
z+=a[l+1:]

print(z)

