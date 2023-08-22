
# To find number of words

fc = open("myfile.txt","r")
s1 = fc.read()
nw = len(s1.split())
print("Total number of words :",nw)


# Function to find the longest line in the file
def count_Longest_Line(filename):
    fid = open(filename)
    l = fid.readlines()

    longest = ""
    for line in l:
        if(len(line) > len(longest)):
           longest = line

    print("Longest Line =",len(longest))
    print(longest)

count_Longest_Line("temp.txt")
