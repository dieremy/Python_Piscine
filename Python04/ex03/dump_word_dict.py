import pickle

def count_word_len(filename):
    word_lengths = {}
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            length = len(word)
            if length in word_lengths:
                word_lengths[length] += 1
            else:
                word_lengths[length] = 1
    return word_lengths

file_name = "words.txt"
word_count_dict = count_word_len(file_name)

#A pickle file
#is a binary file format used in Python
#to serialize and deserialize Python objects.
with open("word_count.pickle", "wb+") as pickle_file: #"wb" write mode in binary
    pickle.dump(word_count_dict, pickle_file)
