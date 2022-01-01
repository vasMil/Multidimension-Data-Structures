class Segment:
    def __init__(self, pt1, pt2):
        if pt1 > pt2:
            self.pt1 = pt1
            self.pt2 = pt2
        else:
            self.pt1 = pt2
            self.pt2 = pt1

    def __gt__(self, other):
        if self.getHigherPriorityPoint().x > other.getHigherPriorityPoint().x:
            return True
        return False

    def __lt__(self, other):
        if self.getHigherPriorityPoint().x < other.getHigherPriorityPoint().x:
            return True
        return False

    def __eq__(self, other):
        if self.getHigherPriorityPoint().x == other.getHigherPriorityPoint().x:
            return True
        return False

    def __repr__(self):
        return self.toString()

    def getLowerPriorityPoint(self):
            return self.pt2

    def getHigherPriorityPoint(self):
        return self.pt1

    def toString(self):
        return '{' + self.pt1.toString() + ', ' + self.pt2.toString() + '}'

    def print(self):
        print(self.toString())