mylist = ['Solapur', 'Mumbai', 'Pune', 'Bengaluru', 'Kolhapur']
try:
    num = int(input('ENTER NUMERATOR - '))
    den = int(input('ENTER DENOMINATOR - '))

    result = num // den
    print(result)
    print(mylist[result])
except ZeroDivisionError as e:
    print('YOU CANNOT DIVIDE ANY NUMBER BY ZERO')
except ValueError as e:
    print('INVALID INPUT FOR NUMERATOR OR DENOMINATOR')
except IndexError as e:
    print(e)