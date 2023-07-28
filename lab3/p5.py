n = int(input())
flag = 1
for i in range(2,n+1,1):
    if(n%i==0 and n != i):
        print("Not a prime number")
        flag = 0
        break
if(flag != 0):    
    print("Prime number")

