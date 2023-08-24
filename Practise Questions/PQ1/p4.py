#Abe is going to plant „m‟ oak trees and „n‟ pine trees. Abe would like to plant the trees
#in rows that all have the same number of trees and are made up of only one type of
#tree. What is the greatest number of trees Abe can have in each row? Write a recursive
#function to find the solution.
#
def max_trees_in_row(m, n):
    if n == 0:
        return m
    return max_trees_in_row(n, m % n)

# Get input for number of oak and pine trees
m = int(input("Enter the number of oak trees (m): "))
n = int(input("Enter the number of pine trees (n): "))

# Calculate the greatest number of trees in each row
result = max_trees_in_row(m, n)

# Print the result
print("The greatest number of trees in each row:", result)
