n = int(input("ENTER A NUMBER - "))
   
isprime = True

if n==1:
    isprime = False
x = n//2    
for i in range(2,x+1):
    if n%i==0:
        isprime = False
        
if isprime:
    print(f'{n} IS PRIME NUMBER')
else:
    print(f'{n} IS NOT A PRIME NUMBER')