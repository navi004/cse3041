#Problem - 1 
#reverse the number and subtract from original
a = int(input("Enter the number :"))
r = 10*(a%10)+a/10
r = int(r)
print("Reverse : ",r)
ans = abs(a-r)
print("Difference :",ans)
