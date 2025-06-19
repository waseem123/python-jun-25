a = 10
b = 5
c = 3

print(a>b and a>c) #(True and True => True)
print(a<b and a>c) #(False and True => False)
print(a>b and a<c) #(True and False => False)
print(a<b and a<c) #(False and False => False)
print("_______________")

print(a<b or a<c) #(False or False => False)
print(a<b or a>c) #(False or True => True)
print(a>b or a<c) #(True or False => True)
print(a>b or a>c) #(True or True => True)
print("______________")

print(not(a>b))
print(not(a>b and a>c))
print(a>b and not(a<c))
print(not(a>b and (a<c)))