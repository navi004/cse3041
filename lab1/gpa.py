#write a program to segregate student based on cgpa .the details are as follows :
""" <=9 cgpa <= 10 - outstanding
    <=8 cgpa < 9 - excellent
    <= 7 cgpa < 8 - good
    <= 6 cgpa < 5 - better
    cgpa < 5 - poor"""
def cgpa_segregation():
    n = int(input("Enter the number of students: "))
    i = 1  
    while i in range(1, n):
        cgpa = float(input("Enter the CGPA: "))
        if cgpa > 10 or cgpa < 0:
            print("Invalid CGPA")
        else:
            if 9 <= cgpa <= 10:
                print("Outstanding")
            elif 8 <= cgpa < 9:
                print("Excellent")
            elif 7 <= cgpa < 8:
                print("Good")
            elif 6 <= cgpa < 7:
                print("Better")
            elif 5 <= cgpa < 6:
                print("Below Average")
            elif cgpa < 5:
                print("Poor")
        i += 1

cgpa_segregation()
