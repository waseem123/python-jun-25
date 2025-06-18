a = 10
b = 5
c = 3

print(a>b and a>c)
print(a<b and a>c)
print(a>b and a<c)
print(a<b and a<c)
print("_______________")

print(a<b or a<c)
print(a<b or a>c)
print(a>b or a<c)
print(a>b or a>c)
print("______________")

print(not(a>b))
print(not(a>b and a>c))
print(a>b and not(a<c))
print(not(a>b and (a<c)))