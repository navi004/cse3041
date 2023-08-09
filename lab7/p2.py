
#Problem - 2
#to sort the list without using sort
n = int(input("Enter n: "))
lst = []

for i in range(n):
    val = int(input("Enter the values : "))
    lst.append(val)

for x in range (n):
    for y in range(n-1):
        if(lst[y] > lst[y+1]):
            lst[y],lst[y+1] = lst[y+1],lst[y]
            """temp = lst[y]
            lst[y] = lst[y+1]
            lst[y+1] = temp"""
print(lst)
