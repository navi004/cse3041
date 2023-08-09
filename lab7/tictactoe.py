#Tic tac toe

row =col = 3

tic = [[int(input("Enter the values 0 or 1:")) for j in range(col)] for i in range(row)]

#Check for rows
for i in range(3):
    if(tic[i][0] == 1 or tic[i][1] == 1 or tic[i][2] == 1):
        winner = tic[i][0]
#Check for colums
for i in range(3):
        if(tic[0][i] == 1 or tic[1][i] == 1 or tic[2][i] == 1):
            winner = tic[0][i]
#Check for rows
for i in range(3):
    if(tic[i][0] == 2 or tic[i][1] == 2 or tic[i][2] == 2):
        winner = tic[i][0]
#Check for colums
for i in range(3):
        if(tic[0][i] == 2 or tic[1][i] == 2 or tic[2][i] == 2):
            winner = tic[0][i]

# for diagonals
if(tic[1][1] == 1 or tic[2][2] == 1 or tic[0][0] == 1):
    winner = 1
if(tic[1][1] == 2 or tic[2][2] == 2 or tic[0][0] == 2):
    winner = 2
if
