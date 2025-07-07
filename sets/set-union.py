set1 = {'Mango','Apple','Banana','Orange','Dragon'}
set2 = {'Kiwi','Dragon','Watermelon','Orange','Grapes'}

# 1. Using union function
set3 = set1.union(set2)
print(set1)
print(set2)
print(set3)
print("______________")

# 2. Using update function
set2.update(set1)
print(set1)
print(set2)
print("______________")