def printdata(**info):
    print(info)
    print(f'My name is {info["name"]}')
    print(f'My name is {info["city"]}')
    
printdata(name='Roger',city='LA',age=25)
