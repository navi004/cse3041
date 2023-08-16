phy = [111,153,173,534,245]
maths = [234,363,356,173,890]
chem = [345,111,234,534,890]
cse = [568,353,363,363,733]

phy_s = set(phy)
math_s = set(maths)
chem_s = set(chem)
cse_s = set(cse)

print("Total failures number of failures is :")
set1 = phy_s|math_s|chem_s|cse_s
print(len(set1))


s1 = {1,3,5,6,7,3}
s2 = {2,4,6,7,89}
s1 = s2
s2.clear()
print(s2)
print(s1)


#Dictionary
#(key,value)
#always in pair

#empty dictionary
#does not follow order

dictionary = {}
mydict = {1:'chocolate',2:'Ice cream'}
print(mydict)

students = {'22mia1049' : 'Naveen','22mia1024' : 'Chandra','22mia1064' : 'Yasir','22mia1015' : 'Pavan'}
print(students)
print(students.keys())
print(students.values())
print(students['22mia1049'])

n = int(input("Enter of students: "))
d = {}
for i in range(n):
    regno = input("Enter Regd no :")
    name = input("Enter name :")
    d[regno] = name
print(d)
