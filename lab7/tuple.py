

#list []

#tuple () - immutable objects
#sort cannot be applied  - sort function cannot be used

# list to tuple viceversa
#l = list(t)     t is tuple
#t = tuple(l)

#we cannot individual from tuple but we can delete the tuple whole by using del

t1 = ()
n = int(input("Enter N:"))
for i in range(n):
    s =int(input())
    t1 = t1 + (s,)

t2 = ()
for i in t1:
    if(i%5==0):
        t2 = t2+(i,)
print("Multiples of 5 are ")
print(t2)

#Tuple

t = ()
n = int(input())
for i in range(0,n):
    s = int(input())
    t = t+(s,)
print(t)


