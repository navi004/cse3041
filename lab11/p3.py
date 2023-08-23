#Student class with name and age as attributes.then create a list of students
# and display their names in increasing order of age
class student:
    counter = 0
    def __init__(self,a,n):
        self.full_name = n
        self.age = a
        student.counter = student.counter + 1  


s = []
m = int(input("Enter the number of students :"))
for i in range(0,m):
    name = input("Enter the name :")
    age = int(input("Enter the age :"))
    stud = student(name,age)
    s.append(stud)
print(s)
for i in range(0,m):
    print("Name",s[i].full_name," Age:",s[i].age)


