#Functions
def avg(n1,n2,n3):
    return (n1+n2+n3)/3.0

result = avg(10,20,30)
print(result)


a,*b = 10,20,30
print(b)
l,*m,n = 5,15,25,35
print(n)
print(m)
"""
[20, 30]
35
[15, 25] """


def func(*t):
    print(t)
    print(t[5])

def func2(**d):
    print(d)

func(1,2,3,'abcd',5.7,"Z")

func2(a=1,b=2,c=[4,5,6],f="ABCD",g=89.6)

def func4(a,b,c=3):  #c is called default arguements
    return(a+b+c)
print(func4(10,20))
print(func4(10,20,30))
