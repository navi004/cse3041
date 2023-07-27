#Reversing numbers with strings
def reverse(number):
    num = str(number)
    reverse = num[::-1]
    reverse_num = int(reverse)
    print("Reverse of ",number,"is",reverse_num)

n = int(input())
reverse(n)

#without strings
def reverse(number):
    reverse_num = 0
    while(number != 0):
        last_digit = number%10
        reverse_num = reverse_num*10 + last_digit
        number = number//10
    return reverse_num

number = int(input("Enter the number : "))
print("Reversed number of",number,"is",reverse(number))

