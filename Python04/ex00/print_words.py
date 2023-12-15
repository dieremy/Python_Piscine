char_len = int(input("Insert an integer: "))
f = open("words.txt")

lst = list(f)
f.close()

for elem in lst :
    word = elem.strip("\n")
    length = len(word)
    ind = word.find(" ")
    if length >= char_len :
        if ind != -1 :
            print(word[0:ind])
        else :
            print(word)
