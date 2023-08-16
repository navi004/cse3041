#sets are immutable
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Automatically removes duplicate values
#cannot use index
x = {1,2,3,4}
y ={"apple","ball","cat"}
x1 = set('spam')
print(x1)

#Union
s1 = {1,2,3,4}
s2 = {4,5,6,7}
s3 = s1 | s2
print(s3)

#Intersection
s4 = s1 & s2
print(s4)

#Reading values of sets
n = int(input("Enter the number of elements in s1 :"))
s = set()
for i in range(n):
    val = int(input("Enter number :"))
    s.add(val)   #s | {val}
print(s)
print(len(s))
