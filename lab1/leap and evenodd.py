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
