
#To check given points form a triangle
import math
def func1(x1,y1,x2,y2,x3,y3):
    if(x1 == x2 == x3):
        return False
    elif(y1 == y2 == y3):
        return False
    else:
        return True
def func2(x1,y1,x2,y2,x3,y3):
    x12 = math.pow((x2-x1),2) + math.pow((y2-y1),2)
    x13 = math.pow((x3-x1),2) + math.pow((y3-y1),2)
    x23 = math.pow((x2-x3),2) + math.pow((y2-y3),2)

    l1 = math.sqrt(x12)
    l2 = math.sqrt(x13)
    l3 = math.sqrt(x23)
    if(l1 == l2 == l3):
        return False
    else:
        return True
def func3(x1,y1,x2,y2,x3,y3):
    if(func1(x1,y1,x2,y2,x3,y3)):
       if(func2(x1,y1,x2,y2,x3,y3)):
          area = abs((1/2)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
          print(area)

func3(1,4,2,6,6,8)


