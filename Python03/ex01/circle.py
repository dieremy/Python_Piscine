class Point :

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point) :

    def __init__(self, p, radius) :
        self.p = p
        self.radius = radius

    def __str__(self) :
        Point.__init__(self.p.x, self.p.y)
        return "Circle of center (%s, %s) and radius %s" % (Point.x, Point.y, self.radius)

def main() :
    lst = []
    lst.append(150)
    lst.append(100)

    p = Point(int(150), int(100))
    print(type(p))
    print(p.x, p.y)
    c = Circle(p, 75)
    print(c)

if __name__ == "__main__" :
    main()
