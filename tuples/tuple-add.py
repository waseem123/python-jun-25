demo = (20,40,60,80,100)
print(demo)
# demo.insert(2,650)

# Tuple insertion using list conversion method
demolist = list(demo)
demolist.insert(2,650)
print(demolist)
demo = tuple(demolist)
print(demo)

# demo[3] = 45

# demo.pop()

# del demo[1]

# demo.clear()

del demo
print(demo)