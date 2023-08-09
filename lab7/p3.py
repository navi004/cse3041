#Problem - 2
#to check the sum of any two number in a list is equal to the given number
#without repetition in a list

m = int(input("Enter M : "))
n = int(input("Enter N : "))
nlst = []
for x in range(n):
    val = int(input("Enter the price of flavours : "))
    nlst.append(val)
for i in range(n):
    for j in range(i,n):
        if(i != j):
            if((nlst[i] + nlst[j]) == m):
                print(i,j)
