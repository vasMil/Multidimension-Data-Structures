class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return True
        return False

    def __lt__(self,other):
        if(self.y < other.y):
            return True
        elif(self.y == other.y and self.x > other.x):
            return True
        return False

    def __gt__(self, other):
        if(self.y > other.y):
            return True
        elif(self.y == other.y and self.x < other.x):
            return True
        return False

    def __repr__(self):
        return self.toString()

    def toString(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def print(self):
        print(self.toString())
