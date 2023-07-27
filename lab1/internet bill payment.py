
#Problem - 3
#Internet Browsing Bill Calculation
hrs = int(input("Enter Hours : "))
mins = int(input("Enter min : "))

if(hrs > 7 or mins > 60):
    print("Invalid")
else:
    if(hrs >= 5):
        total = 200 + 50*(hrs-5) + mins
        print(total)
    else:
        total = hrs*50 + mins
        print(total)
