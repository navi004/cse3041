

# taking total sum
fp = open("marks.csv","r+")
fp.seek(0)
l = []
line = fp.readline()
heading = line
while True:
    line = fp.readline()
    if not line:
        break
    line = line.replace("\n","")
    st = line.split(",")
    totalsum = int(st[1]) + int(st[2]) + int(st[3])
    st.append(totalsum)
    l.append(st)
fp.close()
