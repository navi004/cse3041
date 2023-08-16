#pass or fail

l1 = ["Naveen","22mia1049",64,78,98]
l2 = ["Bot","22mia0000",23,54,10]

def calculator(l):
    avg = ((l[2]+l[3]+l[4])/3)
    if(avg >= 59):
        print(l[1]+" is Pass")
        l.append(avg)
        l.append("Pass")
    else:
        print(l[1]+"is Fail")
        l.append(avg)
        l.append("Fail")

calculator(l1)
print(l1)
