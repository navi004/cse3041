#Factorial
a = int(input("Enter the number))
result  = 1 
while(1):
    result = a * result
    a = a-1
    if(a<=0):
        print(result)
        break
