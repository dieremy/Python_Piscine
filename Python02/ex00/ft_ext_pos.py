import sys

def print_max(array) :
    max = array[1]
    index = -1
    x = 1
    while x < len(array) :
        v = array[x]
        if (max < v) :
            max = v
            index = x
        x += 1
    print("The max is", max, "and its position is", index)

def print_min(array) :
    min = array[1]
    index = -1
    x = 1
    while x < len(array) :
        v = array[x]
        if (min < v) :
            min = v
            index = x
        x += 1
    print("The min is", min, "and its position is", index)


if (len(sys.argv) == 1) :
    print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
else :
    print_min(sys.argv)
    print_max(sys.argv)
