
"""s = r'a\n\ob\n\oc'
print(s)
print(len(s))

str = 'There are %d %s birds:'%(5,"beautiful")
print(str)

k = 5
str1 = 'There are %d birds:'%k
print(str1)

str2 = 'That is {0} {1} bird!'.format(1,'dead')
print(str2)"""

#name = (input())

"""print(name.upper())
print(name.isupper())    #immutable

print(name.lower())
print(name.islower())

print(len(name))"""

"""total = 0
for x in name:
    print(x)
    total = total + (ord(x))
print("sum of the ASCII is ",total)"""

sname = "naveen"
##print("Number of e s in name ",sname.count('e'))
"""count = 0
sname.lower()
for x in sname:
    if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x =='u'):
        count = count + 1
print(count)

print(sname.count('a')+sname.count('e')+sname.count('i')+sname.count('o')+sname.count('u'))"""

"""count1 = 0
for i in sname:
    if i in :
        count = count1 + 1
print(count1)"""

"""s = input("Enter the name :")
n = len(s)
#Positive index
print(s[0])
print(s[n-1])
#Negative Index
print(s[-n])
print(s[-1])"""

"""name = input()
print(name[0:4:1])
print(name[-7:-1:2])
print(name[::-1])"""

#Palindrome
"""s = input()
n = len(s)
if(s[::-1] == s):
    print("%s is Palindrome"%s)
else:
    print("%s is not a Palindrome"%s)"""

#Pan card validation
pnum = input("Enter the PAN card Number : ")

if(len(pnum) == 10):      ##10 digit constraint
    chars = pnum[0:5:1]         
    digits = pnum[5:9:1]
    if(chars.isalpha()):        ##is alpha
        if(chars.isupper()):        ##is uppercase
            if(digits.isdigit()):       ## is digit
                print("valid PAN card")
else:
    print("Not valid PAN card")
