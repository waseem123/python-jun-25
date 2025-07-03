# Tuples are immutable, ordered, indexed collection of the data
# They also allow the repeated values
# Tuples are represented using ()

#method 1 to create tuple
mytuple = (100,200,300,400,500)
print(mytuple)
print(type(mytuple))

#method 2 - Constructor method to create tuple
demo = tuple(mytuple)
print(demo)
print(type(demo))


print(demo[0])
print(demo[4])

for i in demo:
    print(i)
    
for i in range(len(demo)):
    print(f'{i} -> {demo[i]}')