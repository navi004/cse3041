
#Problem - 1 Regex Expression
"""
# valid PAN number
# valid mobile number
# format for integer number
# format for float number
"""


#PAN Card Validation

import re
pattern1 = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
pan_no = input("Enter the PAN : ")
print("Valid" if re.match(pattern1,pan_no) else "Not Valid")

#Mobile Number

pattern2 = r"^[1-9][0-9]{9}$"
phNo = input("Enter the number : ")
print("Valid Mobile Number" if re.match(pattern2,phNo) else "Invalid Mobile Number")

#Format Integer

"""
   ^     :  Asserts the start of the string.
   \-?   :  Matches an optional minus sign ("-") at the beginning of the string, allowing for negative integers.
  [0-9]+ :  Matches one or more digits (0 to 9).
    $    :  Asserts the end of the string.
"""

patternInt = r"^\-?[0-9]+$"
num =input("Enter an Integer : ")
print("Integer" if re.match(patternInt,num) else "Not an Integer")

#Format Float

patternfl = r"^\-?[0-9]+[.]{1}[0-9]+$"
fl = input("Enter an float number : ")
print("Float" if re.match(patternfl,fl) else "Not a float")
