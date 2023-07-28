n = int(input("Enter the number of students : "))
i=1
sum = 0
while(i<=n):
    mark = int(input("Enter the mark of student  : "))
    if(mark < 0):
        print("Invalid input")
        i = i-1
    else:
        sum = sum + mark 
        i = i+1
average = sum/n
print("Average of class is",average)
