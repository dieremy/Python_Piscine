import sys

def reverse_string(string) :
    new = ""
    for c in range(len(string), 0, -1):
        new += string[c - 1]
    return (new)

def is_palindrome(string) :
    new_string = reverse_string(string)
    return (string == new_string)

def main() :
    if (len(sys.argv) != 2) :
        print("Error! Insert just 1 string!")
    else :
        if (is_palindrome(sys.argv[1]) == True) :
            print("The string", sys.argv[1], "is palindrome")
        elif (is_palindrome(sys.argv[1]) == False) :
            print("The string", sys.argv[1], "is not palindrome")

if __name__ == "__main__" :
    main()
