class MyRoom:
    def __init__(self):
        self.length = int(input("Enter the Lenghth :"))
        self.breadth = int(input("Enter the Breadth: "))

    def Calculate_Area(self):
        area = self.length*self.breadth
        print("Area of the room is:",area,"cm")


R1 = MyRoom()
print(R1.length,R1.breadth)
R1.Calculate_Area()

R2 = MyRoom()
print(R2.length,R2.breadth)
R2.Calculate_Area()
