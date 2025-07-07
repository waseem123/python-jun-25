set1 = {'Mango','Apple','Banana','Orange','Dragon'}
set2 = {'Kiwi','Dragon','Watermelon','Orange','Grapes'}

# 1. using difference function
set3 = set1.symmetric_difference(set2)
print(set1)
print(set2)
print(set3)
print("______________")

# 2. using symmetrict_difference_update function
set2.symmetric_difference_update(set1)
print(set1)
print(set2)
print("______________")