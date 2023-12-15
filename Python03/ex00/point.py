class Point :

    def __init__(self, x1, x2, y1, y2) :
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def distance(self) :
        return (((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)

def main() :

    input_x = input("Insert the coordinates of the first point: ").split()
    input_y = input("Insert the coordinates of the second point: ").split()
    x = input_x[0].split(",")
    y = input_y[0].split(",")
    #print(x, y)
    p = Point(float(x[0]), float(x[1]), float(y[0]), float(y[1]))
    print("Their distance is:", p.distance())

#CHECK THIS FUNCTION CAUSE IS NOT WORKING AS EXPECTED 
if __name__ == "__main__" :
    main()
