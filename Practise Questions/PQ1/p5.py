#TO remove the punctutaions in a given passage

def remove_punctuation(passage):
    l = len(passage)
    new = ""
    for i in range(l):
        if passage[i] == "'":
            continue
        else:
            new += passage[i]  # Use += to concatenate characters
    print(new)

p = input()
remove_punctuation(p)
