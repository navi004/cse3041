#staircase with nested for loop

h = int(input())
if(h > 0):
    for i in range(1,h+1,1):
        for i in range(1,i+1,1):
            print("#",end='')
        print(" ")
