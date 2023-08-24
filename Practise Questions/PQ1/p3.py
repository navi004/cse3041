#Customer rating feedback segregation based on age
n = int(input("Enter the number of customers:"))
l1 = []
l2 = []
for i in range(n):
    name = input("Enter the name:")
    age = int(input("Enter the age:"))
    rating = float(input("Enter the rating:"))
    c_details = (name,age,rating)
    
    if(age <= 20):
        l1.append(c_details)
    else:
        l2.append(c_details)


for i in range(len(l1)):
    for j in range(len(l1)-1):
        if(l1[j][2] > l1[j+1][2]):
            l1[j],l1[j+1] = l1[j+1],l1[j]

for i in range(len(l2)):
    for j in range(len(l2)-1):
        if(l2[j][2] > l2[j+1][2]):
            l2[j],l2[j+1] = l2[j+1],l2[j]
            
print("List 1 (Under age 20)")
print("Name   Age Rating")
for i in l1:
    print(i[0],i[1],i[2])
    
print("List-2 (Above age 20)")
print("Name   Age Rating")
for i in l2:
    print(i[0],i[1],i[2])
