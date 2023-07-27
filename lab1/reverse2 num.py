#Problem - 1 
#reverse the number and subtract from original
"""a = int(input("Enter the number :"))
r = 10*(a%10)+a/10
r = int(r)
print("Reverse : ",r)
ans = abs(a-r)
print("Difference :",ans)"""

#Probelem-2
#If Statement
"""mark1 = int(input("Enter Mark1 : "))
mark2 = int(input("Enter Mark2 :"))

if(mark1 >= 90 and mark2 >= 90):
    print("Excellent")
elif(mark1 >= 90 or mark2 >= 90):
    if(mark1 < 50 or mark2 < 50):
        print("Need to take special classes")
    else:
    print("Good")
elif(mark1 < 90 and mark2 < 90):
    print("Need to improve")"""

#Problem - 3
#Internet Browsing Bill Calculation
"""hrs = int(input("Enter Hours : "))
mins = int(input("Enter min : "))

if(hrs > 7 or mins > 60):
    print("Invalid")
else:
    if(hrs >= 5):
        total = 200 + 50*(hrs-5) + mins
        print(total)
    else:
        total = hrs*50 + mins
        print(total)"""

#Max of two numbers
"""a = int(input("a : "))
b = int(input("b : "))
if(a > b):
    print("a is greater than b")
elif(b > a):
    print("b is greater than a")
else:
    print("a is equal to b")
    
max = a if(a>b) else b
print(max)"""

#Write a python code to check whether a given number of odd or even ?
a = int(input("Enter  :"))
if(a%2 == 0):
        print("Even")
else:
    print("Odd")
    
#write a python  code to check whether a given year is leap year or not?
year = int(input("Enter year : "))
if(year%100==0 and year%400==0):
    print("Leap Year")
elif(year%4==0 and year%100==0):
    print("Leap Year")
else:
    print("Non - Leap Year")
    
#to find the roots of a quadratic equation
import math

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

print("Expression is", a, "x^2 +", b, "x +", c)

# Calculate the discriminant (b^2 - 4ac)
discriminant = b*b - 4*a*c

# Check if the discriminant is non-negative (real roots exist)
if discriminant >= 0:
    # Calculate the two roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    print("No real roots exist for the given quadratic equation.")


#write a program to segregate student based on cgpa .the details are as follows :
""" <=9 cgpa <= 10 - outstanding
    <=8 cgpa < 9 - excellent
    <= 7 cgpa < 8 - good
    <= 6 cgpa < 5 - better
    cgpa < 5 - poor"""

#While
"""i = 1
while i < 10:
    print(i,end=' ')
    i+=1"""
#Factorial
"""a = int(input())
result  = 1 
while(1):
    result = a * result
    a = a-1
    if(a<=0):
        print(result)
        break"""
#Reverese
a = int(input())
reverse  = 0
while(a <= 0):
    reverse = reverse + 10*(a%10) + a//10
    a = a//10
print(reverse)

"""while("""
a = a[::-1]
print
