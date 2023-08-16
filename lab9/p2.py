#LEGB

#Global Scope
x = 99

def func(y):
    #x = 79
    z = x + y
    return z

print(func(1))

#Factorial

def factorial(n):
    fact = 1
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))
    
#GCD
def gcd(m,n,i=1):

    i=min(m,n)
    if(m%i==0 and n%i==0):
        return i
    else:
        i = i-1
        return gcd(m,n,i)

print(gcd(100,60))





def hcf(a,b):
    if(b==0):
        return(a)
    else:
        return hcf(b,a%b)

print(hcf(60,100))
