x = ('a1','a2','a3')
y = 500

mydict = dict.fromkeys(x,y)
print(mydict)

mydict = {'id': 101, 
          'name': 'John', 
          'city': 'San Fransisco', 
          'salary': 20000, 
          'designation': 'Data Scientist',
          'workingdays':25
        }
print(mydict)
mydict.setdefault('workingdays',0)
print(mydict['workingdays'])
