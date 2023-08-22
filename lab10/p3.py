

#Copying from one file to another
f1 = open("temp.txt","r+")
s1 = f1.read()
f1.close()

f2 = open("empty.txt","w+")
f2.write(s1)
f2.close()

print("File copied")

