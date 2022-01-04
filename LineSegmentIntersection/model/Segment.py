from env.constants import MINIMUM_DISTANCE_FROM_ZERO as eps

class Segment:
    def __init__(self, pt1, pt2):
        if pt1 > pt2:
            self.pt1 = pt1
            self.pt2 = pt2
        else:
            self.pt1 = pt2
            self.pt2 = pt1
        self.compData = self.pt1.x

    def __gt__(self, other):
        if self.compData > other.compData:
            return True
        return False

    def __lt__(self, other):
        if self.compData < other.compData:
            return True
        return False

    def __eq__(self, other):
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        return False

    def __repr__(self):
        return self.toString()


    # Given the current y coordinate of the sweep line, update the x-axis value you store in Segment (compData)
    # so you may "swap" the segments that intersect, inside the status tree T.
    def updateComparissonData(self, sweep_line_y):
        yl_eps = sweep_line_y - eps
        if yl_eps <= self.pt2.y:
            # Since eps is the smallest value I may represent (defined in env), there cannot be a point between
            # sweep_line_y and sweep_line_y - eps thus I may use the x of the point with the lowest y coord
            # as compData - avoids some unecessary (unsafe) computation in the case the sweepline is super close or
            # on the lowest point of the segment
            self.compData = self.pt2.x
            return
        xdif = self.pt2.x - self.pt1.x
        ydif = self.pt2.y - self.pt1.y
        if not ydif:
            return
        self.compData = ((yl_eps - self.pt1.y)*xdif) / ydif + self.pt1.x


    def includes(self, point):
        xdif = self.pt2.x - self.pt1.x; ydif = self.pt2.y - self.pt1.y
        if (point.y - self.pt1.y)*xdif - point.x + ydif*self.pt1.x < eps:
            return True
        return False


    def toString(self):
        return '{' + self.pt1.toString() + ', ' + self.pt2.toString() + '}'

    def print(self):
        print(self.toString())