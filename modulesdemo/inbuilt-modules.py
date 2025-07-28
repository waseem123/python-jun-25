import random as r

print(r.randint(1, 10))
print(r.randrange(500,600))
print(r.randrange(1000,10000))

mylist = ['Uzma','Sadiya','Hayyan','Tarannum','Waseem']

print(r.choice(mylist))
r.shuffle(mylist)

print(mylist)