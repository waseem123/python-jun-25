# 5! = 5*4*3*2*1
#     = 5 * 4!
#     4! = 4*3!
#     3! = 3*2!
#     2! = 2*1!
#     1! = 1   
# n! = n*(n-1)!

def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))