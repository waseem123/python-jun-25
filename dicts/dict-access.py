mydict = {'id': 101, 'name': 'John', 'city': 'San Fransisco', 'salary': 20000, 'designation': 'Data Scientist'}
print(mydict)

for i in mydict:
    print(f'{i} -> {mydict[i]}')
print("________________")
for i in mydict.values():
    print(i)
print("________________")

for i in mydict.items():
    print(i[0],'->',i[1])
print("________________")

for i,j in mydict.items():
    print(i,'->',j)
    