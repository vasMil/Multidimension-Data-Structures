class Segment:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1;
        self.pt2 = pt2;

    def getLowerPriorityPoint(self):
        if (self.pt1.y < self.pt2.y):
            return self.pt1
        elif (self.pt1.y == self.pt2.y):
            return self.pt1.x > self.pt2.x if self.pt1 else self.pt2

    def getHigherPriorityPoint(self):
        if (self.pt1.y > self.pt2.y):
            return self.pt1
        elif (self.pt1.y == self.pt2.y):
            return self.pt1.x < self.pt2.x if self.pt1 else self.pt2

    def toString(self):
        return '{' + self.pt1.toString() + ', ' + self.pt2.toString() + '}'

    def print(self):
        print(self.toString())