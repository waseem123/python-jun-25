set1 = {'Mango','Apple','Banana','Orange','Dragon'}
set2 = {'Kiwi','Dragon','Watermelon','Orange','Grapes'}

# 1. using difference function
set3 = set1.difference(set2)
print(set1)
print(set2)
print(set3)
print("______________")

# 2. using - operator
set4 = set2 - set1
print(set1)
print(set2)
print(set4)
print("______________")

# 3. using difference_update function
set2.difference_update(set1)
print(set1)
print(set2)
print("______________")
