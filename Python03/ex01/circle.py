class Point :
    def __init__(self, lst):
        self.lst = lst

class Circle :

    def __init__(self, p, radius) :
        self.p = p
        self.radius = radius

    def __str__(self) :
        return "Circle of center(%s, %s) and radius %s" % (self.p.lst[0], self.p.lst[1], self.radius)

def main() :
    lst = []
    lst.append(150)
    lst.append(100)

    p = Point(lst)
    c = Circle(p, 75)
    print(c)

if __name__ == "__main__" :
    main()
