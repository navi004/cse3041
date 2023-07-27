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
