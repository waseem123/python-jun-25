mylist = ['One Plus', 'iPhone', 'Redmi', 'Nothing', 'RealMe', 'Nokia']
print(mylist)

mylist.sort(reverse=True)
print(mylist)

mylist.reverse()
print(mylist)

print(mylist.count('RealMe'))

print(mylist.index('RealMe'))

yourlist = ['Lava','Micromax','Karbon','Moto']
datalist = yourlist + mylist
print(datalist)

yourlist.extend(mylist)
print(mylist)
print(yourlist)

print(mylist*10)

print(mylist[::1])