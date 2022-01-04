from env.constants import MINIMUM_DISTANCE_FROM_ZERO as eps
import math

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
        self_angle = self.getAngle()
        other_angle = other.getAngle()
        if self.compData == other.compData and self_angle > other_angle:
            return True
        if self.compData == other.compData and self_angle == other_angle and self.pt2 < other.pt2:
            return True
        if self.compData == other.compData and self_angle == other_angle and self.pt2 == other.pt2 and self.pt1 > other.pt1:
            return True
        return False

    def __lt__(self, other):
        if self.compData < other.compData:
            return True
        self_angle = self.getAngle()
        other_angle = other.getAngle()
        if self.compData == other.compData and self_angle < other_angle:
            return True
        if self.compData == other.compData and self_angle == other_angle and self.pt2 > other.pt2:
            return True
        if self.compData == other.compData and self_angle == other_angle and self.pt2 == other.pt2 and self.pt1 < other.pt1:
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
    def updateComparissonData(self, sweep_line_y, last_x_checked_by_sweep_line):
        yl_eps = sweep_line_y - eps
        if yl_eps <= self.pt2.y:
            # Since eps is the smallest value I may represent (defined in env), there cannot be a point between
            # sweep_line_y and sweep_line_y - eps
            # Thus I may use the the x value of the current event point + eps
            # as compData - if that value is out of the segment, use the x coordinate of the furthest point
            # on the segment.
            # - Chose this so I may detect intersections that are caused by overlaps like ---o---x---o---b---b---x---
            # - Watch segments s1,s2,s3 on Test3 for segmentIntersection
            self.compData = last_x_checked_by_sweep_line + eps
            maxx = max(self.pt1.x, self.pt2.x)
            if self.compData > maxx: self.compData = maxx
            return
        xdif = self.pt2.x - self.pt1.x
        ydif = self.pt2.y - self.pt1.y
        if not ydif:
            return
        self.compData = ((yl_eps - self.pt1.y)*xdif) / ydif + self.pt1.x


    def includes(self, point):
        if self.pt1.x == self.pt2.x:
            if self.pt1.y >= point.y and self.pt2.y <= point.y: return True
        m = (self.pt2.y - self.pt1.y) / (self.pt2.x - self.pt1.x)
        b = self.pt1.y - m*self.pt1.x
        y = m*point.x +b
        if  y - point.y < eps:
            return True
        return False


    def getAngle(self):
        return math.atan(self.getSlope())


    def getSlope(self):
        xdif = self.pt2.x - self.pt2.x
        if not xdif:
            return math.inf
        return (self.pt2.y - self.pt2.y) / xdif


    def toString(self):
        return '{' + self.pt1.toString() + ', ' + self.pt2.toString() + '}'

    def print(self):
        print(self.toString())