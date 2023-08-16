#Factorial

def factorial(n):
    fact = 1
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))
    
