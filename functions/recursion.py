def printvalue(num):
    if num>0:
        print(num)
        printvalue(num-1)
    
printvalue(5)