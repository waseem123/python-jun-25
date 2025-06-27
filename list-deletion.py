mylist = ['Samsung', 'One Plus', 'Oppo', 'iPhone', 'Redmi', 'Nothing', 'Vivo', 'RealMe', 'Nokia', 'BlackBerry', 'Infinix','Nokia','Nokia','Nokia']
print(mylist)

# delete from end
mylist.pop()
print(mylist)
mylist.pop()
print(mylist)

#Deleting the data at any index
mylist.pop(2)
print(mylist)
mylist.pop(5)
print(mylist)
del mylist[0]
print(mylist)

# Deletion of specific value from list
mylist.remove('Nokia')
print(mylist)
# mylist.remove('Nokia')
# print(mylist)
# mylist.remove('Nokia')
# print(mylist)

# To empty the list
mylist.clear()
print(mylist)

del mylist
print(mylist)