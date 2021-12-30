class Segment:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2

    def __gt__(self, other):
        if(self.getHigherPriorityPoint().x > other.getHigherPriorityPoint().x):
            return True
        return False

    def __lt__(self, other):
        if(self.getHigherPriorityPoint().x < other.getHigherPriorityPoint().x):
            return True
        return False

    def __eq__(self, other):
        if(self.getHigherPriorityPoint().x == other.getHigherPriorityPoint().x):
            return True
        return False

    def __repr__(self):
        return self.toString()

    def getLowerPriorityPoint(self):
        if (self.pt1 < self.pt2):
            return self.pt1
        else:
            return self.pt2

    def getHigherPriorityPoint(self):
        if (self.pt1 > self.pt2):
            return self.pt1
        else:
            return self.pt2

    def toString(self):
        return '{' + self.pt1.toString() + ', ' + self.pt2.toString() + '}'

    def print(self):
        print(self.toString())