def read_words(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.append(line)
    file.close()
    return words

file_name = input("Insert file name: ")

try :
    words = read_words(file_name)
    words.sort()

    char_len = int(input("Insert an integer: "))
    print("The words longer than", char_len, "are the following:")
    for elem in words :
        word = elem.strip("\n")
        length = len(word)
        ind = word.find(" ")
        if length >= char_len :
            if ind != -1 :
                print(word[0:ind])
            else :
                print(word)
except FileNotFoundError:
    print("Error! The specified file does not exist!")
