#Read
f1 = open("temp.txt","r")
content = f1.read()
print(content)

f1 = open("temp.txt","r")
while True:
    line = f1.readline()
    if not line:
        break
    print(line)
  
f1 = open("temp.txt","r")
l = []
while True:
    line = f1.readlines()
    l.append(line)
    if not line:
        break
    print(l)

#Write
#Write
fw = open("temp.text","w")
fw.write("I am good boy")
fw.close()

fw2 = open("temp.text","w")
lines_of_text = ["a line of text","another line of text","a third line"]
fw2.writelines(lines_of_text)
fw2.close()

fw3 = open("temp.txt","a")
fw3.write("Hello World")
fw3.close()




