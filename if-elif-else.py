a = 510
b = 500
c = 50000

if a>b and a>c:
    print(f'{a} is greater than {b} and {c}')
elif b>a and b>c:
    print(f'{b} is greater than {a} and {c}')
elif c>a and c>b:
    print(f'{c} is greater than {a} and {b}')
else:
    print("ANY NUMBER IS EQUAL TO ANOTHER")