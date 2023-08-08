#find num whose left is equal to right
n = int(input("Enter the n value : "))
wlist = []

for i in range(n):
    val = int(input("Enter the numbers : "))
    wlist.append(val)
for x in range(n):
    if(sum(wlist[x+1:n]) == sum(wlist[0:x])):
        print("element is",wlist[x],"index is",x)

    

