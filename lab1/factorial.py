#Factorial
a = int(input("Enter the number : "))
result  = 1
b = a
if(a == 0):
    print("Factorial of 0 is 1")
elif(a<0):
    print("Factorial doesnot exist for negative number")
else:
    while(1):
        result = a * result
        a = a-1
        if(a<=0):
            print("Factorial of ",b,"is",result)
            break


#With for loop
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
