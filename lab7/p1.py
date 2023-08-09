
#Aug 9 Problem -1 
#to combine to lists and sort it and print it
n = int(input("Enter n :"))
p = int(input("Enter p :"))
s1 = []
s2 = []
for i in range(n):
    val = int(input("Enter values in S1 : "))
    s1.append(val)
for x in range(p):
    val2 = int(input("Enter values in S2 : "))
    s2.append(val2)
#s1.extend(s2) can also be used 
s = s1+s2
s.sort()
print(s)
