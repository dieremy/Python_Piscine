a = input("Insert a string: ")
b = int(input("Insert an integer: "))

if (b > len(a)) :
    print("Error: index out of range")
else :
    print(a[b : (len(a) + 1) - b])
