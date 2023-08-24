"""
The DNA sequence is made up of four chemical bases, Adenine (A), Cytosine (C),
Thymine (T), and Guanine (G). For a given DNA sequence like
“ATCTCAGTCGTTGTCTACATGA”, write a program to count the number of
Adenine, Cytosine, Thymine, and Guanine. Read any input from user and print the
output as dictionary which stores the Alphabet as key and its frequency as value.

Example:
Input:
AAGGTAAGTTGA

Output:
'G': 4, 'A': 5, 'C': 0, 'T': 3

"""
#Problem - 1
seq = input("Enter the Sequence :")
S = seq.upper()
countA = 0
countT = 0
countC = 0
countG = 0
for i in S:
    if(i == 'A'):
        countA = countA +  1
    elif(i == 'C'):
        countC = countC+1
    elif(i == 'G'):
        countG = countG + 1
    elif(i == 'T'):
        countT = countT + 1
    else:
        print("Invalid Sequence")
        break
print("'G':",countG,",'A':",countA,",'C':",countC,",'T':",countT)
