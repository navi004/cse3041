#File Handling
"""
#Modes
read - r+
write - w+
append - a+
"""
#file and code in same location
f1 = open("temp.txt","r")
print("Name of the file : ",f1.name)
print("Closed or not :",f1.closed)
print("Opening mode :",f1.mode)

#file and code in different locations
f2 = open("/home/ex5/something/sometext.txt","r")
print("Name :",f2.name)
print("Closed or not :",f2.closed)
print("Opening mode :",f2.mode)
