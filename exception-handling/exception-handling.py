try:
    num = int(input('ENTER NUMERATOR - '))
    den = int(input('ENTER DENOMINATOR - '))

    result = num / den
    print(result)
except ZeroDivisionError as e:
    print('YOU CANNOT DIVIDE ANY NUMBER BY ZERO')
