class Event:
    def __init__(self, point):
        self.point = point
        self.upperPointArr = []
        self.lowerPointArr = []
        self.LiesInsideArr = []

    def __gt__(self, other):
        if (self.point > other.point):
            return True
        return False

    def __lt__(self, other):
        if (self.point < other.point):
            return True
        return False

    def __eq__(self, other):
        if (self.point == other.point):
            return True
        return False

    def appendUpperPoint(self, segment):
        self.upperPointArr.append(segment)

    def appendLowerPoint(self, segment):
        self.lowerPointArr.append(segment)

    def appendLiesInside(self, segment):
        self.LiesInsideArr.append(segment)