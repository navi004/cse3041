#Class and Objects

class student:
    #A simple example
    i = 12345

    def f(self):
        return "Hello World"
    def adds(self,a,b):
        return a+b

#constructor    
    def __init__(self,n,a):
        self.fullname = n
        self.age = a



s1 = student("Naveen",19)
s2 = student("neevaN",91)
print(s1.age)
print(s2.age)
 
