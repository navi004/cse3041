N = int(input("Enter N : "))
lst = []
for i in range(N):
    val = int(input("Enter the marks : "))
    lst.append(val)
np = 0
nn = 0
nz = 0
for x in lst:
    if(x == 0):
        nz+=1
    elif(x>0):
        np+=1
    elif(x<0):
        nn+=1
print("No of zeroes is ",nz)  #count(0) can also be used
print("No of positive numbers is ",np)
print("No of negatives is ",nn)
