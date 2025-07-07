set1 = {'Mango','Apple','Banana','Orange','Dragon','Kiwi','Watermelon','Grapes'}
set2 = {'Mango','Apple','Banana'}
set3 = {'Kiwi','Dragon','Watermelon','Orange','Grapes'}

print(set1.issuperset(set2))
print(set2.issubset(set1))
print(not(set2.isdisjoint(set3)))
