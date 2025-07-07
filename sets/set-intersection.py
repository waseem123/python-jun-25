set1 = {'Mango','Apple','Banana','Orange','Dragon'}
set2 = {'Kiwi','Dragon','Watermelon','Orange','Grapes'}

# 1. using intersection function
set3 = set1.intersection(set2)
print(set1)
print(set2)
print(set3)
print("______________")

# 2. Using intersection_update function
set2.intersection_update(set1)
print(set1)
print(set2)
print("______________")