n = 151
temp = n
reverse = 0
while temp!=0:
    rem = temp % 10
    print(rem)
    reverse = (reverse*10)+rem
    temp= temp//10

print(reverse)

if n==reverse:
    print("Number is Palindrome")
else:
    print("NUMBER IS NOT PALINDROME")