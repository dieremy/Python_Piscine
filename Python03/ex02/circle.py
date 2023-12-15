import sys

class Point :
    def __init__(self, lst):
        self.lst = lst

class Circle :

    def __init__(self, p, radius) :
        self.p = p
        self.radius = radius

    def contains(p) :
        dis = (((p.x - 0) ** 2 + (p.y - 0) ** 2) ** 0.5)
        if 1.0 - dis < 1.0000000 :
            return 0
        return 1

        

    def __str__(self) :
        return "Circle of center(%s, %s) and radius %s" % (self.p.lst[0], self.p.lst[1], self.radius)

def main() :
    if len(sys.argv) != 3 :
        print("Error! Wrong number of arguments")
    else :
        point_x = float(sys.argv[1])
        point_y = float(sys.argv[2])
        print(point_x, point_y)

if __name__ == "__main__":
    main()
