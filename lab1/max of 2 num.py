#Max of two numbers
a = int(input("a : "))
b = int(input("b : "))
if(a > b):
    print("a is greater than b")
elif(b > a):
    print("b is greater than a")
else:
    print("a is equal to b")
    
max = a if(a>b) else b
print(max)
