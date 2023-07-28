 # m and n are two different kind of apple with kgs m,n.HCF of the boxes of the m,n apples
n = int(input("Enter m : "))
m = int(input("Enter n : "))
for i in range(min(m,n),0,-1):
    if(m%i==0 and n%i==0):
        print("Volume of the Box(HCF) is ",i)
        break
