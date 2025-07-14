def isprime(num):
    if num==1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(isprime(5))
print(isprime(15))
print(isprime(7))
print(isprime(50))
print(isprime(1))