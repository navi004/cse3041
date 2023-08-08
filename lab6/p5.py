List of names
"""lst = []
N = int(input("Enter N : "))

for i in range(N):
        val = (input("Enter the names : "))
        lst.append(val)
print(lst)


print(lst[0],lst[N-1])

print(lst[2:4])"""

#to create a list of even numbers
#lst = list(range(0,100,2))
#print(lst)
#print(lst[4:13])

"""l = [0,1,[34,42]]
print(l[2][0])"""

#list1 + list2 - concatenation
#L1 * L2 - cross join

#l1 = ['carlo','andy','sara','victor']
"""N = int(input("Enter N : "))
lst = []
for i in range(N):
    val = int(input("Enter the marks : "))
    lst.append(val)"""

"""sum = 0
i=0
for i in range(N):
    sum = lst[i] + sum
average = sum/N
print(average)"""
"""np = 0
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
print("No of negatives is ",nn)"""


#find num whose left is equal to right
n = int(input("Enter the n value : "))
wlist = []

for i in range(n):
    val = int(input("Enter the numbers : "))
    wlist.append(val)
for x in range(n):
    if(sum(wlist[x+1:n]) == sum(wlist[0:x])):
        print("element is",wlist[x],"index is",x)

