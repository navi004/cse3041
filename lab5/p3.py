#Problem 1 Ceaser cipher
"""The Caesar cipher is a simple substitution cipher, 
where each letter in the plaintext is shifted a fixed number of positions down the alphabet. 
In this case, the key for the shift is set to 3.
"""

s = input("Enter message: ")
key = 3

for i in s.lower():
    
    c = (ord(i)-97 + key)%26
    c = chr(c+97)

    print(c,end="")
