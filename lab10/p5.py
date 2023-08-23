

# reading content from csv file and calculating the total marks
fp = open("marks.csv","r+")
fw = open("empty.txt","w+")
fp.seek(0)
l = []
line = fp.readline()
heading = line
heading = heading.replace("\n","")
fw.write(heading+",Total\n")
while True:
    line = fp.readline()
    if not line:
        break
    line = line.replace("\n","")
    st = line.split(",")
    totalsum = int(st[1]) + int(st[2]) + int(st[3])
    fw.write(line+","+str(totalsum)+"\n")
fp.close()
fw.close()
