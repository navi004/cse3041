#Aug 9 
#List Comprehension
#N = 5
l1 = [int(input())for i in range(N)]
print(l1)


#res = [ord(c) for c in "spam"]
#print(res)

#Lst = [65,75,34,56,33]
#res1 = [chr(c) for c in Lst]
#print(res1)

row = col = 3

#list1 = [0 for j in range(5)]

MatrixA = [[0 for j in range(col)] for i in range(row)]
print(*MatrixA,sep="\n")
