mydict = {
    'id': 101, 
    'name': 'John', 
    'city': 'San Fransisco',
    'age':25,
    'salary':20000,
    'designation':'Data Scientist'
}
print(mydict)

mydict.pop('age')
print(mydict)

mydict.popitem()
print(mydict)

del mydict['city']
print(mydict)

mydict.clear()
print(mydict)

del mydict
print(mydict)