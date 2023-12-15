class Point :

    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1: Point, p2: Point) :
    return (((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5)

def main() :
    p1_input = input("Insert the coordinates of the first point: ")
    p2_input = input("Insert the coordinates of the second point: ")

    x, y = p1_input.split(",")
    j, k = p2_input.split(",")
    try :
        p1 = Point(float(x), float(y))
        p2 = Point(float(j), float(k))
    except Exception as e :
        print("Error")
        exit(1)

    print("Their distance is:", distance(p1, p2))

#CHECK THIS FUNCTION CAUSE IS NOT WORKING AS EXPECTED 
if __name__ == "__main__" :
    main()
