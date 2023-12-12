import sys

v = int(sys.argv[1])
if (len(sys.argv) != 2) :
    print("Error! Usage: python3 ft_summorial.py <n>")
elif (v < 0) :
    print("Error! n must be >=0")
elif (v == 0) :
    print("The sum is:", v)
else :
    r = 0
    for i in range(1, v + 1) :
        r += i
    print("The sum is:", r)
