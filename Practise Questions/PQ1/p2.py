#Convert the first letter of each word to capital in a given sentence
s = input("Enter the input sentence:")
words = s.split()
C_words = []
for word in words:
    C_words.append(word.capitalize())
S = ' '.join(C_words)
print(S)
        
