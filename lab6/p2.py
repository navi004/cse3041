#List of names
lst = []
N = int(input("Enter N : "))

for i in range(N):
        val = (input("Enter the names : "))
        lst.append(val)
print(lst)


print(lst[0],lst[N-1])

print(lst[2:4])

