
#tuple
n = 5
testR = ()
minv = (20,35.5,12,120,80)
maxv = (30,40,15,150,120)

for i in range(0,5):
    s = input()
    testR = testR + (s,)
    
print(testR)

for j in range(0,5):
    if(testR[j] == "N"):
        print("Test "+str(j+1)+" is not performed")
        continue
    if(float(testR[j])>=minv[j] and float(testR[j])<=maxv[j]):
        print("Test "+str(j+1)+" are normal")
    else:
        print("Test result "+str(j+1)+"are abnormal")
