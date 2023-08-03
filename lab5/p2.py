
#Problem - 2 Regular Expression
"""
<2Xnumber><3Xalpha><4Xnumber>
"""
import re
pattern = r"^[1-9][0-9][a-zA-Z]{3}[0-9]{4}$"
regNo = input("Enter the RegdNo :")
print("Valid"if re.match(pattern,regNo) else "Not Valid")
