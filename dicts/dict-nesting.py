employees = {
    'e1':{
            'id':101,'name':'xyz'
        },
    'e2':{
            'id':102,'name':'LMN'
        },
    'e3':{
            'id':103,'name':'PQR'
    }
}
print(employees)
print(employees['e2'])
print("___________________________")

d1 = {
        'id':101,'name':'xyz'
    }
d2 = {
        'id':102,'name':'PQR'
    }
d3 = {
        'id':103,'name':'LMN'
    }

mydict = {
    'dict1':d1,
    'dict2':d2,
    'dict3':d3
}

print(mydict)

mylist = [d1,d2,d3]
print(mylist)

print(mydict['dict3'])