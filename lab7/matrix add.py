
#Nested list - Matrix printing
#n = int(input("Enter the n :"))
row = col = 3
MatrixA = [[int(input("Enter the number : ")) for j in range(col)] for i in range(row)]

#print(*MatrixA,sep="\n") can be used 

for x in MatrixA:
    print(x)



row = int(input("Enter rows :"))
col = int(input("Enter cols :"))

row2 = int(input("Enter rows :"))
col2 = int(input("Enter cols :"))


mat1 = [[int(input("Enter1 :")) for j in range(col)] for i in range(row)]
mat2 = [[int(input("Enter2 :")) for j in range(col2)] for i in range(row2)]

if(row != row2 and col != col2):
    print("Cannot be added")
    

else:
    summat = [[0 for j in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            summat[i][j] = mat1[i][j] + mat2[i][j]
            
print(*summat,sep="\n")
