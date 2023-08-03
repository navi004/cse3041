
#Problem - 2 Regular Expression
"""
<2Xnumber><3Xalpha><4Xnumber>
"""
"""
^:               Asserts the start of the string.
[1-9]:           Matches any digit from 1 to 9 (ensuring the registration number doesn't start with 0).
[0-9]:           Matches any digit from 0 to 9.
[a-zA-Z]{3}:     Matches exactly three alphabetic characters (both uppercase and lowercase letters are allowed).
[0-9]{4}:        Matches exactly four digits.
$:               Asserts the end of the string.
"""
import re
pattern = r"^[1-9][0-9][a-zA-Z]{3}[0-9]{4}$"
regNo = input("Enter the RegdNo :")
print("Valid"if re.match(pattern,regNo) else "Not Valid")
