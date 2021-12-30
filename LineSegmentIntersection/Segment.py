class Segment:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1;
        self.pt2 = pt2;

    def getLowerPriorityPoint(self):
        return self.pt1 < self.pt2 if self.pt1 else self.pt2

    def getHigherPriorityPoint(self):
        return self.pt1 > self.pt2 if self.pt1 else self.pt2

    def toString(self):
        return '{' + self.pt1.toString() + ', ' + self.pt2.toString() + '}'

    def print(self):
        print(self.toString())