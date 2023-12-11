a = input("Insert a string: ")
b = int(input("Insert an interger: "))

if (b > len(a)) :
    print("Error: index out of range")
else :
    letter = a[b]
    next_to_last_ind = b - 1
    next_to_last_letter = a[next_to_last_ind]
    print(letter, next_to_last_letter)
